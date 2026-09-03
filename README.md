# Financial Report Multi-Agent

An AI application for analyzing financial information from Japanese securities reports.

## Project Overview

This project explores an AI-based financial analysis system using large language models (LLMs).

The project starts with a prototype that uses multiple specialized analysis components to analyze different aspects of a company's financial and business information.

The system will be developed into a multi-agent architecture, where multiple specialized agents independently analyze different aspects of a company's financial and business information.

## Current Status

The prototype currently performs:

1. Extract financial and business sections from an annual securities report
2. Generate financial analysis
3. Generate business and industry analysis
4. Integrate both analyses for internal credit assessment
5. Generate a lending decision and monitoring points

## Architecture

PDF
→ Section Extraction
→ Financial Analysis + Business Analysis
→ Credit Assessment Orchestration
→ Lending Decision

### Project Structure

```text
financial_report_multi_agent/

├── prototype/
│   ├── main.py
│   ├── pdf_reader.py
│   ├── analyzer.py
│   ├── business_analyzer.py
│   └── orchestration.py
│
├── .gitignore
└── README.md
```