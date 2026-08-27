from pathlib import Path
from dotenv import load_dotenv

from pdf_reader import read_financial_section
from analyzer import analyze_financial_statement


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

PDF_PATH = BASE_DIR / "data" / "S100YIG2.pdf"


financial_text = read_financial_section(PDF_PATH)

analysis = analyze_financial_statement(financial_text)

print(analysis)
