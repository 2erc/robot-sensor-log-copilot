import streamlit as st

from log_parser import parse_log_text

st.set_page_config(
    page_title="Robot / Sensor Log Copilot",
    page_icon="🤖",
)

st.title("Robot / Sensor Log Copilot")
st.write("Upload a robot log and get an AI-assisted analysis.")

uploaded_file = st.file_uploader(
    "Upload a .txt log file",
    type=["txt"],
)

if uploaded_file is not None:
    log_text = uploaded_file.getvalue().decode("utf-8")

    st.subheader("Raw log")
    st.text(log_text)

    issues = parse_log_text(log_text)

    st.subheader("Extracted issues")
    st.json(issues)
