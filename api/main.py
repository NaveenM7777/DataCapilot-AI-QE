from fastapi import FastAPI, HTTPException

from api.schemas import SQLQueryRequest, SQLQueryResponse
from api.services import ask_sql_agent

app = FastAPI(title="DataCapilot-AI API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sql/query", response_model=SQLQueryResponse)
def sql_query(request: SQLQueryRequest):
    try:
        result = ask_sql_agent(request.question)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    return SQLQueryResponse(question=request.question, **result)