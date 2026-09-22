# Robot / Sensor Log Copilot

A lightweight Streamlit app that extracts warnings and errors from robot logs and uses DeepSeek to provide debugging suggestions.

## Features

- Upload a UTF-8 `.txt` robot log
- Extract `WARNING` and `ERROR` entries
- Skip malformed log lines
- Send structured issues to DeepSeek for analysis
- Display user-friendly errors when file decoding or API calls fail

## Tech Stack

- Python 3.12
- Streamlit
- DeepSeek API
- OpenAI-compatible Python SDK
- pytest

## Local Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

Copy the environment variable template:

```bash
cp .env.example .env
```

Then replace `your_api_key_here` in `.env` with your DeepSeek API key.

## Run the App

```bash
streamlit run streamlit_app.py
```

Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Run Tests

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the tests:

```bash
python -m pytest -v
```

## Sample Data

A sample robot log is available at `sample_data/motor_log.txt`.

## Current Limitations

- Only UTF-8 `.txt` files are supported
- Log entries must use the `timestamp | level | module | message` format
- Only `WARNING` and `ERROR` entries are extracted
- LLM suggestions may be incomplete or inaccurate and should be verified
