# Financial Report Multi-Agent

An AI application for analyzing financial information from Japanese securities reports.

## Project Overview

This project explores an AI-based financial analysis system using large language models (LLMs).

The project starts with a single-agent prototype that extracts the financial section of a securities report and generates a financial analysis using Google Gemini.

The system will be developed into a multi-agent architecture, where multiple specialized agents analyze different aspects of a company's financial and business information.

## Current Status

The current version is a single-agent prototype.

The prototype:

1. Reads a PDF securities report
2. Extracts the financial section
3. Sends the extracted information to an LLM
4. Generates a financial analysis

### Project Structure

```text
financial_report_multi_agent/

├── prototype/
│   ├── main.py
│   ├── pdf_reader.py
│   └── analyzer.py
│
├── .gitignore
└── README.md
```