from dataclasses import dataclass


@dataclass(frozen=True)
class HeaderPolicy:
    name: str
    description: str
    recommendation: str


HEADER_POLICIES = (
    HeaderPolicy(
        name="Strict-Transport-Security",
        description="Instructs browsers to use HTTPS for future requests.",
        recommendation=(
            "Consider enabling HSTS when the site is fully prepared "
            "to operate over HTTPS."
        ),
    ),
    HeaderPolicy(
        name="Content-Security-Policy",
        description=(
            "Controls which sources browsers are allowed to load for "
            "different types of content."
        ),
        recommendation=(
            "Review the CSP against the application's actual resource "
            "requirements. A complete CSP audit is outside this tool's scope."
        ),
    ),
    HeaderPolicy(
        name="X-Content-Type-Options",
        description=(
            "Prevents browsers from MIME-sniffing a response away from "
            "the declared Content-Type."
        ),
        recommendation=(
            "Set X-Content-Type-Options to nosniff."
        ),
    ),
    HeaderPolicy(
        name="Referrer-Policy",
        description=(
            "Controls how much referrer information browsers include "
            "when making requests."
        ),
        recommendation=(
            "Review the policy against the application's privacy and "
            "functionality requirements."
        ),
    ),
    HeaderPolicy(
        name="Permissions-Policy",
        description=(
            "Controls access to selected browser features and APIs."
        ),
        recommendation=(
            "Define an appropriate Permissions-Policy based on the "
            "features the application actually needs."
        ),
    ),
    HeaderPolicy(
        name="X-Frame-Options",
        description=(
            "Controls whether a page can be embedded in a frame."
        ),
        recommendation=(
            "Consider an appropriate framing policy. CSP frame-ancestors "
            "should also be considered for modern applications."
        ),
    ),
)