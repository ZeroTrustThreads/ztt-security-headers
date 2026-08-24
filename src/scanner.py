from src.checker import check_headers
from src.http_client import fetch_headers


def scan(url: str) -> dict:
    """
    Perform a security header scan.

    This is the main coordinator for the scanning workflow.

    Steps:
    1. Retrieve HTTP response headers
    2. Evaluate security headers
    3. Return structured results
    """

    response = fetch_headers(url)

    findings = check_headers(response.headers)

    return {
        "url": response.url,
        "status_code": response.status_code,
        "headers": response.headers,
        "findings": findings,
    }