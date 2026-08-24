from collections.abc import Mapping

from src.models import HeaderResult


def check_header(name: str, value: str | None) -> HeaderResult:
    """
    Evaluate a single HTTP security header.

    Findings are intentionally conservative. A missing header is
    reported as missing, while present headers may require review.
    """

    if value is None:
        return HeaderResult(
            name=name,
            status="missing",
            message=f"{name} is not present.",
        )

    normalized_name = name.lower()
    normalized_value = value.strip().lower()

    if normalized_name == "x-content-type-options":
        if normalized_value == "nosniff":
            return HeaderResult(
                name=name,
                status="pass",
                message="X-Content-Type-Options is set to nosniff.",
            )

        return HeaderResult(
            name=name,
            status="review",
            message=(
                "X-Content-Type-Options is present but does not "
                "use the expected nosniff value."
            ),
        )

    if normalized_name == "strict-transport-security":
        return HeaderResult(
            name=name,
            status="pass",
            message="Strict-Transport-Security is present.",
        )

    if normalized_name == "content-security-policy":
        return HeaderResult(
            name=name,
            status="review",
            message=(
                "Content-Security-Policy is present. A complete CSP "
                "policy review is outside this tool's scope."
            ),
        )

    if normalized_name == "referrer-policy":
        return HeaderResult(
            name=name,
            status="review",
            message=(
                "Referrer-Policy is present. Review the selected "
                "policy against application requirements."
            ),
        )

    if normalized_name == "permissions-policy":
        return HeaderResult(
            name=name,
            status="review",
            message=(
                "Permissions-Policy is present. Review enabled browser "
                "features against application needs."
            ),
        )

    if normalized_name == "x-frame-options":
        return HeaderResult(
            name=name,
            status="review",
            message=(
                "X-Frame-Options is present. Consider the application's "
                "framing requirements and CSP frame-ancestors."
            ),
        )

    return HeaderResult(
        name=name,
        status="info",
        message=f"{name} is present.",
    )


def check_headers(
    headers: Mapping[str, str],
) -> list[HeaderResult]:
    """
    Evaluate all supported security headers.

    Header names are matched case-insensitively because HTTP field
    names are case-insensitive.
    """

    normalized_headers = {
        name.lower(): value
        for name, value in headers.items()
    }

    supported_headers = (
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy",
        "X-Frame-Options",
    )

    return [
        check_header(
            name,
            normalized_headers.get(name.lower()),
        )
        for name in supported_headers
    ]