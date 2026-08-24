from dataclasses import dataclass

import requests


DEFAULT_TIMEOUT = 10


@dataclass(frozen=True)
class HttpResponse:
    url: str
    status_code: int
    headers: dict[str, str]


class HttpClientError(Exception):
    """Raised when an HTTP request cannot be completed."""


def fetch_headers(
    url: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> HttpResponse:
    """
    Fetch HTTP response headers for a URL.

    TLS certificate verification remains enabled.
    Redirects are followed so the checker evaluates the final response.
    """

    try:
        response = requests.get(
            url,
            timeout=timeout,
            allow_redirects=True,
            verify=True,
            headers={
                "User-Agent": "ZTT-Security-Headers/0.1",
            },
        )
        response.raise_for_status()

    except requests.RequestException as exc:
        raise HttpClientError(
            f"Unable to retrieve {url}: {exc}"
        ) from exc

    return HttpResponse(
        url=response.url,
        status_code=response.status_code,
        headers=dict(response.headers),
    )