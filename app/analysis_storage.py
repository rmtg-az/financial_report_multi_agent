import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_PATH = BASE_DIR / "output_json" / "analysis_result.json"


def save_analysis_results(
    financial_analysis: str,
    business_analysis: str,
    lending_analysis: str,
) -> None:

    result = {
        "financial_analysis": financial_analysis,
        "business_analysis": business_analysis,
        "lending_analysis": lending_analysis,
    }

    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)