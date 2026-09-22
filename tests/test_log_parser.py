from log_parser import parse_log_text


def test_parse_log_text_extracts_warning_and_error():
    log_text = (
        "10:00:00 | INFO | SYSTEM | startup complete\n"
        "10:00:01 | WARNING | MOTOR_1 | temperature rising\n"
        "10:00:02 | ERROR | CONTROL | motor stopped"
    )

    issues = parse_log_text(log_text)

    assert len(issues) == 2
    assert issues[0]["level"] == "WARNING"
    assert issues[1]["module"] == "CONTROL"


def test_parse_log_text_skips_malformed_line():
    log_text = (
        "10:00:00 | INFO | SYSTEM | startup complete\n"
        "this line is malformed\n"
        "10:00:02 | ERROR | CONTROL | motor stopped"
    )

    issues = parse_log_text(log_text)

    assert len(issues) == 1
    assert issues[0]["line"] == 3
    assert issues[0]["message"] == "motor stopped"
