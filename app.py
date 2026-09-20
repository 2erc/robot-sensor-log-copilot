with open("sample_data/motor_log.txt", "r", encoding="utf-8") as log_file:
    issues = []
    for line_number, line in enumerate(log_file, start=1):
        clean_line = line.strip()
        try:
            timestamp, level, module, message = clean_line.split(" | ")
        except ValueError:
            print(f"Skipping malformed line {line_number}: {clean_line}")
            continue
        if level in ("WARNING", "ERROR"):
            issues.append(
                {"line": line_number, "timestamp": timestamp, 
                "level": level, "module": module, "message" : message}
            )

    print(f"Found {len(issues)} issues")
    for issue in issues:
        print(issue)