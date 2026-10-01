from pathlib import Path
from dotenv import load_dotenv

from pdf_reader import read_financial_section,read_business_section
from agents.financial_agent import analyze_financial_statement
from agents.business_agent import analyze_business
from agents.lending_agent import analyze_lending
from analysis_storage import save_analysis_results
from chatbot import chat
from logger import save_chat_log


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

PDF_PATH = BASE_DIR / "data" / "S100YIG2.pdf"


financial_text = read_financial_section(PDF_PATH)
business_text = read_business_section(PDF_PATH)

financial_analysis = analyze_financial_statement(financial_text)
business_analysis = analyze_business(business_text)

lending_analysis = analyze_lending(
    financial_analysis=financial_analysis,
    business_analysis=business_analysis
)

save_analysis_results(
    financial_analysis=financial_analysis,
    business_analysis=business_analysis,
    lending_analysis=lending_analysis
)

chat_history=""

print("企業分析が完了しました。")
print("質問を入力してください。")
print("終了する場合は 'exit' と入力してください。")

while True:

    user_question = input("\n質問: ")

    if user_question.lower() == "exit":
        print("終了します。")
        break

    answer = chat(
        user_question=user_question,
        chat_history=chat_history
    )

    print("\n回答:")
    print(answer)

    save_chat_log(
        question=user_question,
        answer=answer
    )

    chat_history += f"""
    質問: {user_question}
    回答: {answer}
    """