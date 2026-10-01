from langchain_google_genai import ChatGoogleGenerativeAI


LLM_MODEL = "gemini-2.5-flash"


def analyze_lending(
    financial_analysis: str,
    business_analysis: str
    ) -> str:

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        temperature=0
    )


    prompt = f"""
あなたは金融機関の法人融資審査を担当する銀行員です。

以下に、対象企業について別のAIエージェントが作成した
「財務分析」と「事業分析」の結果があります。

これらの分析結果を踏まえ、金融機関の立場から対象企業を総合的に評価してください。

【財務分析】
{financial_analysis}

【事業分析】
{business_analysis}

以下の観点から分析してください。

1. 事業面の評価
- 主力事業・収益源は何か
- 事業の強み・競争優位性は何か
- 市場環境や事業上のリスクは何か
- 今後の成長性や収益安定性をどう見るか

2. 財務面の評価
- 収益性
- 財務安全性
- キャッシュフロー
- 借入金・債務負担
- 資金繰り上の懸念
について重要なポイントを整理してください。

3. 融資の観点からの評価
- この企業に融資する場合の主なメリット
- 融資する場合に注意すべきリスク
- 今後確認すべき情報
を整理してください。

4. 総合評価
財務面と事業面を総合的に踏まえ、
「金融機関としてどのような企業と評価できるか」を説明してください。

ただし、与えられた情報だけでは判断できない事項については、
推測で補完せず「追加確認が必要」と明記してください。

また、「融資すべき」「融資すべきでない」と単純に結論づけるのではなく、
融資判断に影響する要因を具体的に説明してください。

分析結果は、銀行員が企業を理解し、融資判断を検討するための
参考情報として整理してください。
"""
    
    response = llm.invoke(prompt)

    return response.content