with open("sample_data/motor_log.txt", "r", encoding="utf-8") as log_file:
    for line_number, line in enumerate(log_file, start=1):
        clean_line = line.strip()
        timestamp, level, module, message = clean_line.split(" | ")
        if level in ("WARNING", "ERROR"):
            print(
                f"Line {line_number}: "
                f"time={timestamp}, level={level}, "
                f"module={module}, message={message}"
                )