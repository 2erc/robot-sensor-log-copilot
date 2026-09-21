from log_parser import parse_log

issues = parse_log("sample_data/motor_log.txt")

print(f"Found {len(issues)} issues")

for issue in issues:
    print(issue)
