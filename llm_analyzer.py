import os

from dotenv import load_dotenv
from openai import OpenAI


def analyze_issues(issues_json):
    load_dotenv()

    api_key = os.getenv("DEEPSEEK_API_KEY")

    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is not set")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
    )
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "You analyze robot and sensor logs. "
                    "Separate observed facts from possible explanations. "
                    "Do not invent events that are not present in the logs."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Analyze the following extracted log issues.\n"
                    "Report: anomalies found, approximate locations, "
                    "items to inspect next, and concise debugging suggestions.\n\n"
                    f"{issues_json}"
                ),
            },
        ],
        max_tokens=800,
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )

    return response.choices[0].message.content
