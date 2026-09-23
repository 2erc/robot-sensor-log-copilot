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
st.caption("Review robot logs and get focused debugging suggestions.")

st.subheader("Upload a log")

uploaded_file = st.file_uploader(
    "Choose a UTF-8 .txt file",
    type=["txt"],
)
st.caption("One entry per line: timestamp | level | module | message")

with open("sample_data/motor_log.txt", "rb") as sample_file:
    st.download_button(
        "Try a sample log",
        data=sample_file,
        file_name="motor_log.txt",
        mime="text/plain",
        type="tertiary",
    )

if uploaded_file is not None:
    try:
        log_text = uploaded_file.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Could not read this file. Please upload a UTF-8 encoded text file.")
        st.stop()

    issues = parse_log_text(log_text)

    st.subheader("Findings")
    if issues:
        st.caption(f"{len(issues)} warning/error entries found")
        st.dataframe(issues, hide_index=True)
    else:
        st.info("No warnings or errors were found in this log.")

    with st.expander("View raw log"):
        st.text(log_text)

    st.subheader("AI analysis")
    analyze_clicked = st.button(
        "Analyze with DeepSeek",
        type="primary",
        disabled=not issues,
    )

    if analyze_clicked:
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
            st.markdown(analysis)
