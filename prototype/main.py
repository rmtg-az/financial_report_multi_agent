from pathlib import Path
from dotenv import load_dotenv

from pdf_reader import read_financial_section,read_business_section
from analyzer import analyze_financial_statement
from business_analyzer import analyze_business
from orchestration import orchestrate_analysis


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

PDF_PATH = BASE_DIR / "data" / "S100YIG2.pdf"


financial_text = read_financial_section(PDF_PATH)

business_text = read_business_section(PDF_PATH)

financial_analysis = analyze_financial_statement(financial_text)

business_analysis = analyze_business(business_text)

credit_analysis = orchestrate_analysis(
    financial_analysis,
    business_analysis
)

print(credit_analysis)
