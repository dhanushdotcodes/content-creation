from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

history = [
        {
            "role": "system",
            "content": "You are a helpful assistant, who tells a random funny knock knock jokes to the user"
        },
        {
            "role": "assistant",
            "content": "knock knock"
        },
        {
            "role": "user",
            "content": "who's there?"
        }
    ]

gpt_mini = client.responses.create(
    model="gpt-4o-mini",
    input=history
)

print(gpt_mini.output_text)

history.append({
    "role": "assistant",
    "content": gpt_mini.output_text
})

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "exit" or user_input.lower() == "quit":
        break
    
    history.append({
        "role": "user",
        "content": user_input
    })

    gpt_mini = client.responses.create(
        model="gpt-4o-mini",
        input=history
    )

    print(gpt_mini.output_text)
    history.append({
        "role": "assistant",
        "content": gpt_mini.output_text
    })