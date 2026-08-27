from pypdf import PdfReader


def read_financial_section(path):
    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    start_keyword = "第５【経理の状況】"
    end_keyword = "第６【提出会社の株式事務の概要】"

    start = text.find(start_keyword)
    end = text.find(end_keyword)

    if start == -1:
        raise ValueError(f"開始キーワードが見つかりません: {start_keyword}")

    if end == -1:
        raise ValueError(f"終了キーワードが見つかりません: {end_keyword}")

    return text[start:end]