from src.database import get_header_info


def format_learning(result) -> str:
    """
    Create an educational explanation for a header finding.
    """

    info = get_header_info(result.name)

    references = "\n".join(
        f"- {item}"
        for item in info.get("references", [])
    )

    return f"""
{result.name}
{'-' * len(result.name)}

Status:
{result.status.upper()}

What is it?
{info.get('purpose')}

Why does it matter?
{info.get('security_benefit')}

Difficulty:
{info.get('difficulty')}

References:
{references}
""".strip()