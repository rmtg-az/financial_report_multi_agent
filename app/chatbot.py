import json
from pathlib import Path

from orchestration import orchestrate_analysis
from rag import retrieve_documents

BASE_DIR = Path(__file__).resolve().parent.parent
ANALYSIS_PATH = BASE_DIR / "output_json" / "analysis_result.json"


def load_analysis_results() -> dict:
    with open(ANALYSIS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def chat(
        user_question: str,
        chat_history: str = ""
    ) -> str:

    analysis = load_analysis_results()

    financial_analysis = analysis["financial_analysis"]
    business_analysis = analysis["business_analysis"]
    lending_analysis = analysis["lending_analysis"]

    docs = retrieve_documents(user_question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    answer = orchestrate_analysis(
        financial_analysis=financial_analysis,
        business_analysis=business_analysis,
        lending_analysis=lending_analysis,
        user_question=user_question,
        chat_history=chat_history,
        rag_context=context
    )

    return answer