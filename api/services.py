def ask_sql_agent(question: str) -> dict:
    """Placeholder. Later this will call the real SQL agent."""
    return {
        "sql": "SELECT 1;",
        "answer": f"(stub) You asked: {question}",
    }


def ask_excel_agent(content: bytes, filename: str, question: str) -> dict:
    """Placeholder. Later this will call the real Excel agent."""
    return {"answer": f"(stub) {filename} has {len(content)} bytes. Q: {question}"}


def ask_pdf_agent(content: bytes, filename: str, question: str) -> dict:
    """Placeholder. Later this will call the real PDF agent."""
    return {"answer": f"(stub) {filename} has {len(content)} bytes. Q: {question}"}