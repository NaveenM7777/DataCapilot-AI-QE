def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
def test_sql_query_returns_answer(client, monkeypatch):
    def fake_agent(question):
        return {"sql": "SELECT COUNT(*) FROM customers;",
                "answer": "There are 42 customers."}

    monkeypatch.setattr("api.main.ask_sql_agent", fake_agent)

    response = client.post("/sql/query", json={"question": "How many customers?"})

    assert response.status_code == 200
    assert response.json() == {
        "question": "How many customers?",
        "sql": "SELECT COUNT(*) FROM customers;",
        "answer": "There are 42 customers.",
    }


def test_sql_query_rejects_empty_question(client):
    response = client.post("/sql/query", json={"question": ""})
    assert response.status_code == 422


def test_sql_query_rejects_missing_question(client):
    response = client.post("/sql/query", json={})
    assert response.status_code == 422


def test_sql_query_handles_agent_failure(client, monkeypatch):
    def broken_agent(question):
        raise RuntimeError("database offline")

    monkeypatch.setattr("api.main.ask_sql_agent", broken_agent)

    response = client.post("/sql/query", json={"question": "hello"})

    assert response.status_code == 500
    assert "database offline" in response.json()["detail"]