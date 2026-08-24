import requests

from src.http_client import (
    HttpClientError,
    HttpResponse,
    fetch_headers,
)


def test_http_response_stores_response_data():
    response = HttpResponse(
        url="https://example.com",
        status_code=200,
        headers={
            "X-Content-Type-Options": "nosniff",
        },
    )

    assert response.url == "https://example.com"
    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"


def test_fetch_headers_returns_response(monkeypatch):
    class FakeResponse:
        url = "https://example.com"
        status_code = 200
        headers = {
            "X-Content-Type-Options": "nosniff",
            "Strict-Transport-Security": "max-age=31536000",
        }

        def raise_for_status(self):
            pass

    def fake_get(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    result = fetch_headers("https://example.com")

    assert result.url == "https://example.com"
    assert result.status_code == 200
    assert result.headers["X-Content-Type-Options"] == "nosniff"


def test_fetch_headers_handles_request_failure(monkeypatch):
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("Connection failed")

    monkeypatch.setattr(requests, "get", fake_get)

    try:
        fetch_headers("https://example.com")
    except HttpClientError as exc:
        assert "Unable to retrieve" in str(exc)
    else:
        raise AssertionError("Expected HttpClientError")


def test_fetch_headers_uses_expected_request_settings(monkeypatch):
    captured = {}

    class FakeResponse:
        url = "https://example.com"
        status_code = 200
        headers = {}

        def raise_for_status(self):
            pass

    def fake_get(*args, **kwargs):
        captured["url"] = args[0]
        captured["kwargs"] = kwargs
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    fetch_headers("https://example.com")

    assert captured["url"] == "https://example.com"
    assert captured["kwargs"]["timeout"] == 10
    assert captured["kwargs"]["allow_redirects"] is True
    assert captured["kwargs"]["verify"] is True
    assert captured["kwargs"]["headers"]["User-Agent"] == (
        "ZTT-Security-Headers/0.1"
    )