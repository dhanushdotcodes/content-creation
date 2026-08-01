from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

gpt_mini = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ]
)

print(gpt_mini.choices[0].message.content)