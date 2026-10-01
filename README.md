# Financial Report Multi-Agent

An AI application for analyzing Japanese corporate financial reports using LLMs, multi-agent architecture, and Retrieval-Augmented Generation (RAG).

## Project Overview

This project explores how large language models (LLMs) can support corporate financial analysis and lending operations at financial institutions.

The application uses multiple specialized agents to analyze a company's financial performance, business conditions, and lending-related risks. It also provides an interactive chat interface that allows users to explore the analysis results and ask follow-up questions using relevant source documents retrieved through RAG.

The goal is to support corporate banking professionals in understanding companies, identifying potential risks, and preparing questions for management interviews.

## Current Features

The current prototype provides the following features:

1. **Financial Analysis**
   Analyzes financial information extracted from annual securities reports.

2. **Business Analysis**
   Analyzes business conditions and relevant industry information.

3. **Lending Analysis**
   Integrates financial and business analyses to identify lending risks and monitoring points.

4. **RAG-based Document Retrieval**
   Retrieves relevant passages from source documents to support responses to user questions.

5. **Interactive Chat**
   Allows users to ask follow-up questions about the analysis results while taking previous conversation history into account.

6. **Analysis Result Storage**
   Saves the outputs of the specialized agents in JSON format so they can be reused during subsequent chat interactions without rerunning the entire analysis pipeline.

7. **Chat Logging**
   Records user questions and AI-generated answers for review and further development.

## Architecture

```text
Annual Securities Report (PDF)
             |
             v
     Section Extraction
             |
      +------+------+
      |             |
      v             v
Financial Agent   Business Agent
      |             |
      +------+------+
             |
             v
       Lending Agent
             |
             v
     Analysis Results (JSON)
             |
             v
      Interactive Chat
             |
      +------+------+
      |             |
      v             v
  RAG Retrieval   Chat History
      |             |
      +------+------+
             |
             v
   LLM-based Response Generation
             |
             v
       Answer & Chat Log
```

## Technology Stack

* **Language:** Python
* **LLM:** Google Gemini 2.5 Flash
* **LLM Integration:** LangChain
* **Document Processing:** pypdf
* **RAG / Embeddings:** Hugging Face Sentence Transformers
* **Vector Search:** FAISS
* **Data Storage:** JSON
* **Environment Configuration:** python-dotenv

## Project Structure

```text
financial_report_multi_agent/
├── app/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── analysis_storage.py
│   ├── chatbot.py
│   ├── orchestration.py
│   ├── rag.py
│   ├── logger.py
│   ├── requirements.txt
│   └── agents/
│       ├── financial_agent.py
│       ├── business_agent.py
│       └── lending_agent.py
├── .gitignore
└── README.md
```

*Note: The project structure may evolve as development progresses.*

## Design Considerations

* **Separation of responsibilities:** Each specialized agent focuses on a distinct analytical task.
* **Efficient iteration:** Intermediate analysis results are saved and reused to avoid unnecessary LLM calls when refining the chat functionality.
* **Evidence-based responses:** Retrieved source documents and analysis results are used to support responses.
* **Fact and inference separation:** Prompts instruct the model to distinguish documented facts, analytical interpretations, and hypotheses.
* **Practical lending support:** The application focuses on identifying relevant risks, follow-up questions, and additional information needed for lending assessments.

## Limitations

* This is an experimental prototype, not a production-ready lending decision system.
* AI-generated analyses and responses may contain inaccuracies and require human verification.
* The quality of retrieval and analysis depends on the source documents, extraction process, prompts, and underlying language models.
* The application does not replace professional judgment or a financial institution's internal credit assessment process.

## Future Development

* Develop a FastAPI-based interface.
* Improve retrieval accuracy and source traceability.
* Refine analytical prompts and response quality.
* Enhance chat history and logging.
* Evaluate the accuracy and practical usefulness of the generated analyses.

## Disclaimer

This project is intended for learning, experimentation, and demonstration purposes. It does not provide investment advice or automated credit approval.

Sample financial reports and API credentials are not included in this repository.
