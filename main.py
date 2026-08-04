import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("OpenRouter API key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    model_id = "openrouter/free"

    messages = [
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ]

    response =  client.chat.completions.create(model=model_id, messages=messages)
    response_message = response.choices[0].message.content


    print(response_message)


if __name__ == "__main__":
    main()
