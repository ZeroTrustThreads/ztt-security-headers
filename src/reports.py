from dataclasses import asdict
import html
import json

from src.database import get_header_info


def results_to_json(scan_result: dict) -> str:
    """
    Convert scan results into educational JSON.
    """

    findings = []

    for result in scan_result["findings"]:
        info = get_header_info(result.name)

        findings.append(
            {
                **asdict(result),
                "education": info,
            }
        )

    output = {
        "target": scan_result["url"],
        "status_code": scan_result["status_code"],
        "findings": findings,
    }

    return json.dumps(
        output,
        indent=4,
    )


def create_html_report(scan_result: dict) -> str:
    """
    Create an educational HTML security report.
    """

    findings_html = ""

    for result in scan_result["findings"]:
        info = get_header_info(result.name)

        references = "".join(
            f"<li>{html.escape(ref)}</li>"
            for ref in info.get("references", [])
        )

        findings_html += f"""
        <section>
            <h2>{html.escape(result.name)}</h2>

            <p>
            <strong>Status:</strong>
            {html.escape(result.status)}
            </p>

            <p>
            <strong>Finding:</strong><br>
            {html.escape(result.message)}
            </p>

            <p>
            <strong>What is it?</strong><br>
            {html.escape(info['purpose'])}
            </p>

            <p>
            <strong>Why does it matter?</strong><br>
            {html.escape(info['security_benefit'])}
            </p>

            <p>
            <strong>Difficulty:</strong>
            {html.escape(info['difficulty'])}
            </p>

            <strong>References:</strong>
            <ul>
            {references}
            </ul>

        </section>

        <hr>
        """

    return f"""
<!DOCTYPE html>
<html>

<head>
<title>ZTT Security Learning Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    margin: 40px;
}}

section {{
    padding: 15px;
}}

h1 {{
    color: #00ff99;
}}

</style>

</head>

<body>

<h1>Zero Trust Threads</h1>

<h2>Security Learning Report</h2>

<p>
<strong>Target:</strong>
{html.escape(scan_result['url'])}
</p>

<p>
<strong>Status Code:</strong>
{scan_result['status_code']}
</p>

<hr>

{findings_html}

</body>

</html>
"""