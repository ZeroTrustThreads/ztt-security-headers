import argparse

from src.http_client import HttpClientError
from src.reports import (
    results_to_json,
    create_html_report,
)
from src.scanner import scan
from src.learning import format_learning


STATUS_SYMBOLS = {
    "pass": "✓",
    "missing": "○",
    "review": "⚠",
    "info": "ℹ",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Assess common HTTP security headers."
    )

    parser.add_argument(
        "url",
        help="URL to assess.",
    )

    parser.add_argument(
        "--learn",
        action="store_true",
        help="Show educational explanations for findings.",
    )

    parser.add_argument(
    "--json",
    action="store_true",
    help="Output results as JSON.",
)

    parser.add_argument(
    "--report",
    choices=["html"],
    help="Generate a report file.",
)

    return parser


def print_results(
    url: str,
    status_code: int,
    results,
    learn: bool = False,
) -> None:
    print()
    print("ZERO TRUST THREADS")
    print("SECURITY HEADERS CHECKER")
    print("=" * 42)
    print()
    print(f"Target: {url}")
    print(f"Status: {status_code}")
    print()
    print("Security Headers")
    print("-" * 42)

    for result in results:
        symbol = STATUS_SYMBOLS.get(result.status, "?")
        print(f"{symbol} {result.name}")
        print(f"  {result.message}")
        print()

        if learn:
            print(format_learning(result))
            print()

    missing = sum(
        result.status == "missing"
        for result in results
    )

    review = sum(
        result.status == "review"
        for result in results
    )

    passed = sum(
        result.status == "pass"
        for result in results
    )

    print("-" * 42)
    print(
        f"Summary: {passed} pass, "
        f"{review} review, "
        f"{missing} missing"
    )


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = scan(args.url)

    except HttpClientError as exc:
        print(f"Error: {exc}")
        return 1

    results = result["findings"]

    if args.json:
        print(results_to_json(result))

    elif args.report == "html":
        filename = (
            result["url"]
            .replace("https://", "")
            .replace("http://", "")
            .replace("/", "-")
        )

        report_path = (
            f"reports/{filename}-report.html"
        )

        with open(
            report_path,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(
                create_html_report(result)
            )

        print(
            f"HTML report created: {report_path}"
        )

    else:
        print_results(
            result["url"],
            result["status_code"],
            results,
            args.learn,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())