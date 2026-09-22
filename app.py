import json

from llm_analyzer import analyze_issues
from log_parser import parse_log


def main():
    issues = parse_log("sample_data/motor_log.txt")
    issues_json = json.dumps(issues, indent=2, ensure_ascii=False)

    print(f"Found {len(issues)} issues")

    print(issues_json)

    analysis = analyze_issues(issues_json)

    print("\nLLM analysis:")
    print(analysis)


if __name__ == "__main__":
    main()
