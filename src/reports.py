from dataclasses import asdict
from pathlib import Path
import json
import html

from src.database import get_header_info


def results_to_json(scan_result: dict) -> str:
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
    findings_html = ""

    for result in scan_result["findings"]:
        info = get_header_info(result.name)

        findings_html += f"""
        <section>
            <h2>{html.escape(result.name)}</h2>

            <p>
            <strong>Status:</strong>
            {result.status}
            </p>

            <p>
            <strong>What is it?</strong><br>
            {info['purpose']}
            </p>

            <p>
            <strong>Why does it matter?</strong><br>
            {info['security_benefit']}
            </p>

            <p>
            <strong>Difficulty:</strong>
            {info['difficulty']}
            </p>
        </section>
        """

    return f"""
<html>
<head>
<title>ZTT Security Learning Report</title>
</head>

<body>

<h1>Zero Trust Threads</h1>
<h2>Security Learning Report</h2>

<p>
Target:
{scan_result['url']}
</p>

<p>
Status Code:
{scan_result['status_code']}
</p>

<hr>

{findings_html}

</body>
</html>
"""