import json
import logging
import streamlit as st

from llm_analyzer import analyze_issues
from log_parser import parse_log_text

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Robot / Sensor Log Copilot",
    page_icon="🤖",
)

st.title("Robot / Sensor Log Copilot")
st.write("Upload a robot log and get an AI-assisted analysis.")

st.subheader("1. Choose a log")
st.write("New here? Download the sample log, then upload it below.")

with open("sample_data/motor_log.txt", "rb") as sample_file:
    st.download_button(
        "Download sample log",
        data=sample_file,
        file_name="motor_log.txt",
        mime="text/plain",
    )

uploaded_file = st.file_uploader(
    "Upload a .txt log file",
    type=["txt"],
)
st.caption(
    "Expected format: timestamp | level | module | message "
    "(one log entry per line)"
)

if uploaded_file is not None:
    try:
        log_text = uploaded_file.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Could not read this file. Please upload a UTF-8 encoded text file.")
        st.stop()

    issues = parse_log_text(log_text)

    st.subheader("2. Review extracted issues")
    st.write(f"Found {len(issues)} warning/error entries.")
    st.json(issues)

    with st.expander("View raw log"):
        st.text(log_text)

    st.subheader("3. Get AI analysis")
    analyze_clicked = st.button(
        "Analyze with DeepSeek",
        type="primary",
    )

    if analyze_clicked:
        if not issues:
            st.warning("No warnings or errors were found in this log.")
        else:
            issues_json = json.dumps(
                issues,
                indent=2,
                ensure_ascii=False,
            )

            try:
                with st.spinner("Analyzing log issues..."):
                    analysis = analyze_issues(issues_json)
            except Exception:
                logger.exception("DeepSeek analysis failed")
                st.error("Analysis failed. Please check the API configuration and try again.")
            else:
                st.subheader("LLM analysis")
                st.markdown(analysis)
