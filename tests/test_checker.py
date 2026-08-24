from src.checker import check_header
from src.policies import HEADER_POLICIES


def test_x_content_type_options_accepts_nosniff():
    result = check_header(
        "X-Content-Type-Options",
        "nosniff",
    )

    assert result.status == "pass"


def test_x_content_type_options_flags_missing_value():
    result = check_header(
        "X-Content-Type-Options",
        None,
    )

    assert result.status == "missing"


def test_x_content_type_options_flags_unexpected_value():
    result = check_header(
        "X-Content-Type-Options",
        "something-else",
    )

    assert result.status == "review"


def test_header_names_are_case_insensitive():
    result = check_header(
        "x-content-type-options",
        "NOSNIFF",
    )

    assert result.status == "pass"


def test_hsts_is_present():
    result = check_header(
        "Strict-Transport-Security",
        "max-age=31536000",
    )

    assert result.status == "pass"


def test_csp_requires_review():
    result = check_header(
        "Content-Security-Policy",
        "default-src 'self'",
    )

    assert result.status == "review"


def test_referrer_policy_requires_review():
    result = check_header(
        "Referrer-Policy",
        "strict-origin-when-cross-origin",
    )

    assert result.status == "review"


def test_permissions_policy_requires_review():
    result = check_header(
        "Permissions-Policy",
        "camera=(), microphone=()",
    )

    assert result.status == "review"


def test_x_frame_options_requires_review():
    result = check_header(
        "X-Frame-Options",
        "SAMEORIGIN",
    )

    assert result.status == "review"


def test_header_policies_include_core_headers():
    policy_names = {
        policy.name
        for policy in HEADER_POLICIES
    }

    expected_headers = {
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "Referrer-Policy",
        "Permissions-Policy",
        "X-Frame-Options",
    }

    assert expected_headers.issubset(policy_names)