from pathlib import Path

import yaml


DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "headers.yaml"
)


def load_header_database() -> dict:
    """
    Load security header educational information.

    Returns:
        Dictionary containing header explanations.
    """

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_header_info(header_name: str) -> dict:
    """
    Retrieve educational information for a security header.
    """

    database = load_header_database()

    return database.get(
        header_name,
        {
            "title": header_name,
            "purpose": "No educational information available.",
            "security_benefit": "No information available.",
            "difficulty": "unknown",
            "references": [],
        },
    )


def list_headers() -> list[str]:
    """
    Return all supported security headers.
    """

    database = load_header_database()

    return list(database.keys())