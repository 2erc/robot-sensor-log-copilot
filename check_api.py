import os

from openai import OpenAI
from dotenv import load_dotenv


def main():
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
                "role": "user",
                "content": "Reply with exactly: API connection successful",
            }
        ],
        max_tokens=20,
        stream=False,
        extra_body={"thinking": {"type": "disabled"}},
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
