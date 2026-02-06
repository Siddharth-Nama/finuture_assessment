# Document 1: Parsing Approach

## Approach Overview
For this assignment, I implemented a **Hybrid Regex-based Extraction** utilizing `pdfplumber` for text ingestion and Python's `re` module for pattern matching.

### 1. Text Extraction (`pdfplumber`)
I chose `pdfplumber` over other libraries (like `PyPDF2` or `pypdf`) because:
- It offers superior layout preservation.
- It handles identifying table structures better (scalability for future table extraction).
- It provides reliable character-level metadata if needed.

### 2. Pattern Matching (Regex)
I used Regular Expressions to identify key fields.
**Why Regex?**
- **Precision**: Insurance documents often follow standard templates (e.g., "Policy No: XXXXX"). Regex allows strict pattern matching.
- **Speed**: Regex is computationally efficient compared to ML/OCR approaches.
- **Deterministic**: The output is predictable and easy to debug.

**Alternative Considered: OCR (Tesseract)**
- OCR is necessary for scanned images but introduces error rates (hallucinations). Since modern insurance policies are usually digital PDFs, straightforward text extraction is more accurate.

**Alternative Considered: LLM/NLP**
- Using an LLM (GPT/BERT) is powerful for unstructured text but introduces latency, cost, and non-determinism. For a specific extraction task, Regex is the standard engineering solution.

## Architecture
- **Backend**: Django + DRF (Standard, Scalable, Secure).
- **Frontend**: React + Vite (Modern, Fast, Component-based).
- **Database**: SQLite (Simple for assignment, easily switchable to PostgreSQL via Django Settings).

### Scalability
The `ParserService` is designed as a standalone class.
- **Future Improvement**: We can implement a "Strategy Pattern" where different Insurance Providers have different `ParserStrategy` classes (e.g., `HDFCParser`, `LICParser`) that inherit from a base `Parser`. The service detects the provider and selects the strategy.
