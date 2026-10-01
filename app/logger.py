from pathlib import Path
import json
import textwrap


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "chat_log.json"


def format_log(text: str, width: int = 80) -> str:
    return textwrap.fill(text, width=width)


def save_chat_log(question: str, answer: str) -> None:

    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    log_entry = {
        "question": format_log(question),
        "answer": format_log(answer),
    }

    logs.append(log_entry)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)