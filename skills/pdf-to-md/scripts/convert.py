from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass
class QualityReport:
    input_pdf: str
    output_md: str
    method: str
    passed: bool
    score: int
    word_count: int
    char_count: int
    heading_count: int
    table_count: int
    replacement_char_count: int
    suspicious_char_ratio: float
    reasons: list[str] = field(default_factory=list)
    attempts: list[dict[str, object]] = field(default_factory=list)
    dependencies: dict[str, bool] = field(default_factory=dict)


def find_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def find_python(repo_root: Path) -> Path:
    candidates = [
        repo_root / ".venv" / "Scripts" / "python.exe",
        repo_root / "venv" / "Scripts" / "python.exe",
        repo_root / ".venv" / "bin" / "python",
        repo_root / "venv" / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return Path(sys.executable)


def module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def default_output_path(input_pdf: Path, output_arg: str | None) -> Path:
    if not output_arg:
        return input_pdf.with_suffix(".md")
    output = Path(output_arg)
    if output.suffix.lower() == ".md":
        return output
    return output / f"{input_pdf.stem}.md"


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def count_tables(lines: list[str]) -> int:
    tables = 0
    for idx in range(len(lines) - 1):
        current = lines[idx].strip()
        nxt = lines[idx + 1].strip()
        if current.startswith("|") and current.endswith("|") and re.match(r"^\|[\s:\-|]+\|$", nxt):
            tables += 1
    return tables


def assess_markdown(input_pdf: Path, output_md: Path, method: str, attempts: list[dict[str, object]]) -> QualityReport:
    text = read_text(output_md)
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    lines = text.splitlines()
    char_count = len(text)
    word_count = len(words)
    heading_count = sum(1 for line in lines if line.lstrip().startswith("#"))
    table_count = count_tables(lines)
    replacement_char_count = text.count("\ufffd")
    suspicious_chars = re.findall(r"[^\w\s.,;:!?()\[\]{}<>/\-+*=#|%$@'\"`~^&\\\n\r\t]", text, flags=re.UNICODE)
    suspicious_char_ratio = len(suspicious_chars) / max(char_count, 1)

    reasons: list[str] = []
    score = 100

    if not output_md.exists():
        reasons.append("output markdown file was not created")
        score -= 80
    if char_count < 1000:
        reasons.append("markdown has fewer than 1000 characters")
        score -= 30
    if word_count < 150:
        reasons.append("markdown has fewer than 150 words")
        score -= 30
    if replacement_char_count:
        reasons.append("markdown contains unicode replacement characters")
        score -= min(30, replacement_char_count)
    if suspicious_char_ratio > 0.08:
        reasons.append("markdown has a high suspicious-character ratio")
        score -= 20

    filename_terms = [
        token.lower()
        for token in re.findall(r"[A-Za-zÀ-ÿ]{4,}", input_pdf.stem)
        if token.lower() not in {"pdf", "para", "com", "gasto"}
    ]
    lower_text = text.lower()
    missing_terms = [term for term in filename_terms[:5] if term not in lower_text]
    if filename_terms and len(missing_terms) == len(filename_terms[:5]):
        reasons.append("none of the filename keywords were found in the markdown")
        score -= 10

    dependencies = {
        "pdfplumber": module_available("pdfplumber"),
        "pypdf": module_available("pypdf"),
        "PyPDF2": module_available("PyPDF2"),
        "fitz": module_available("fitz"),
        "pytesseract": module_available("pytesseract"),
        "pdf2image": module_available("pdf2image"),
        "PIL": module_available("PIL"),
        "tesseract_binary": bool(shutil.which("tesseract")),
    }

    score = max(score, 0)
    passed = score >= 70 and output_md.exists()

    return QualityReport(
        input_pdf=str(input_pdf),
        output_md=str(output_md),
        method=method,
        passed=passed,
        score=score,
        word_count=word_count,
        char_count=char_count,
        heading_count=heading_count,
        table_count=table_count,
        replacement_char_count=replacement_char_count,
        suspicious_char_ratio=round(suspicious_char_ratio, 4),
        reasons=reasons,
        attempts=attempts,
        dependencies=dependencies,
    )


def run_pdfmd(repo_root: Path, python_exe: Path, input_pdf: Path, output_md: Path, extra_flags: list[str]) -> dict[str, object]:
    output_md.parent.mkdir(parents=True, exist_ok=True)
    command = [str(python_exe), "-m", "pdfmd.cli", str(input_pdf), "-o", str(output_md), *extra_flags]
    env = os.environ.copy()
    local_pdfmd = str(repo_root / "pdfmd")
    env["PYTHONPATH"] = local_pdfmd + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    return {
        "method": "pdfmd",
        "returncode": result.returncode,
        "stdout_tail": result.stdout[-1200:],
        "stderr_tail": result.stderr[-1200:],
    }


def fallback_pdfplumber(input_pdf: Path, output_md: Path) -> dict[str, object]:
    if not module_available("pdfplumber"):
        return {"method": "pdfplumber", "skipped": True, "reason": "pdfplumber is not installed"}

    import pdfplumber  # type: ignore

    chunks: list[str] = [f"# {input_pdf.stem}", ""]
    with pdfplumber.open(str(input_pdf)) as pdf:
        for idx, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if text.strip():
                chunks.extend([f"## Page {idx}", "", text.strip(), ""])

    output_md.write_text("\n".join(chunks), encoding="utf-8")
    return {"method": "pdfplumber", "skipped": False, "pages": len(chunks)}


def fallback_pypdf(input_pdf: Path, output_md: Path) -> dict[str, object]:
    reader_cls = None
    module_name = ""
    if module_available("pypdf"):
        from pypdf import PdfReader  # type: ignore

        reader_cls = PdfReader
        module_name = "pypdf"
    elif module_available("PyPDF2"):
        from PyPDF2 import PdfReader  # type: ignore

        reader_cls = PdfReader
        module_name = "PyPDF2"
    else:
        return {"method": "pypdf", "skipped": True, "reason": "pypdf/PyPDF2 is not installed"}

    reader = reader_cls(str(input_pdf))
    chunks: list[str] = [f"# {input_pdf.stem}", ""]
    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            chunks.extend([f"## Page {idx}", "", text.strip(), ""])

    output_md.write_text("\n".join(chunks), encoding="utf-8")
    return {"method": module_name, "skipped": False, "pages": len(reader.pages)}


def fallback_ocr(input_pdf: Path, output_md: Path, lang: str) -> dict[str, object]:
    required = {
        "pdf2image": module_available("pdf2image"),
        "pytesseract": module_available("pytesseract"),
        "PIL": module_available("PIL"),
        "tesseract_binary": bool(shutil.which("tesseract")),
    }
    if not all(required.values()):
        return {"method": "ocr", "skipped": True, "reason": "OCR dependencies are not available", "dependencies": required}

    from pdf2image import convert_from_path  # type: ignore
    import pytesseract  # type: ignore

    chunks: list[str] = [f"# {input_pdf.stem}", ""]
    images = convert_from_path(str(input_pdf))
    for idx, image in enumerate(images, start=1):
        text = pytesseract.image_to_string(image, lang=lang)
        if text.strip():
            chunks.extend([f"## Page {idx}", "", text.strip(), ""])

    output_md.write_text("\n".join(chunks), encoding="utf-8")
    return {"method": "ocr", "skipped": False, "pages": len(images), "lang": lang}


def write_report(report: QualityReport) -> Path:
    report_path = Path(report.output_md).with_suffix(".conversion_report.json")
    report_path.write_text(json.dumps(asdict(report), ensure_ascii=False, indent=2), encoding="utf-8")
    return report_path


def split_wrapper_and_pdfmd_args(argv: list[str]) -> tuple[list[str], list[str]]:
    if "--" not in argv:
        return argv, []
    marker = argv.index("--")
    return argv[:marker], argv[marker + 1 :]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown with offline quality checks and local fallbacks."
    )
    parser.add_argument("input_pdf", help="Input PDF path.")
    parser.add_argument("-o", "--output", help="Output .md file or directory.")
    parser.add_argument("--lang", default="por", help="OCR language when OCR fallback is available.")
    parser.add_argument("--no-fallback", action="store_true", help="Do not attempt local fallbacks after failed validation.")
    wrapper_args, pdfmd_flags = split_wrapper_and_pdfmd_args(argv)
    parsed = parser.parse_args(wrapper_args)
    parsed.pdfmd_flags = pdfmd_flags
    return parsed


def main() -> int:
    args = parse_args(sys.argv[1:])
    repo_root = find_repo_root()
    python_exe = find_python(repo_root)
    input_pdf = Path(args.input_pdf).expanduser().resolve()
    output_md = default_output_path(input_pdf, args.output).resolve()
    extra_flags = args.pdfmd_flags

    attempts: list[dict[str, object]] = []
    if not input_pdf.exists():
        print(f"Input PDF not found: {input_pdf}", file=sys.stderr)
        return 2

    attempts.append(run_pdfmd(repo_root, python_exe, input_pdf, output_md, extra_flags))
    report = assess_markdown(input_pdf, output_md, "pdfmd", attempts)

    if not report.passed and not args.no_fallback:
        for fallback in (fallback_pdfplumber, fallback_pypdf):
            try:
                attempts.append(fallback(input_pdf, output_md))
            except Exception as exc:
                attempts.append({"method": fallback.__name__, "error": str(exc)})
            report = assess_markdown(input_pdf, output_md, attempts[-1].get("method", "fallback"), attempts)
            if report.passed:
                break

    if not report.passed and not args.no_fallback:
        try:
            attempts.append(fallback_ocr(input_pdf, output_md, args.lang))
        except Exception as exc:
            attempts.append({"method": "ocr", "error": str(exc)})
        report = assess_markdown(input_pdf, output_md, attempts[-1].get("method", "ocr"), attempts)

    report_path = write_report(report)
    print(json.dumps({"passed": report.passed, "score": report.score, "output_md": str(output_md), "report": str(report_path)}, ensure_ascii=False))
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
