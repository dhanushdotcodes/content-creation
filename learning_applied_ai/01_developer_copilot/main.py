from openai import OpenAI
from dotenv import load_dotenv
from schema import CalendarEvent

load_dotenv()
    
client = OpenAI()

history = [
    {
        "role": "system",
        "content": "You are a helpful assistant, Who is going answer my questions related to calendar event. And return the response in json format with the keys date, place and description. Please don't answer questions other than the questions related to calendar events."
    }
]

while True:
    user_input = input("User: ")

    if user_input.lower() in {"exit", "quit"}:
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    with client.responses.stream(
        model="gpt-4o-mini",
        input=history,
        text_format=CalendarEvent,
    ) as stream:
        for event in stream:
            if event.type == "response.refusal.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "response.error":
                print(event.error, end="")

        print()

    final_response = stream.get_final_response()
    history.append({
        "role": "assistant",
        "content": final_response.output_text
    })