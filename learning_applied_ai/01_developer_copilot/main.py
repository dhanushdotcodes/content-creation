import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from openai import OpenAI
from dotenv import load_dotenv
from tools import tools
from utils import (
    get_weather,
    get_random_joke,
    get_current_time,
    currency_convertor,
)

load_dotenv()

client = OpenAI()

# Map tool names to actual functions
available_functions = {
    "get_weather": get_weather,
    "get_random_joke": get_random_joke,
    "get_current_time": get_current_time,
    "currency_convertor": currency_convertor,
}

history = [
    {
        "role": "system",
        "content": "You are chatbot assistant with some powerful tools that helps you do many tasks.. Use them when needed"
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

    response = client.responses.create(
        model="gpt-4o-mini",
        input=history,
        tools=tools
    )

    # Tool call loop — keep going until the model gives a text response
    while response.output:
        has_function_call = False

        for item in response.output:
            if item.type == "function_call":
                has_function_call = True
                fn_name = item.name
                fn_args = json.loads(item.arguments)

                print(f"  🔧 Calling {fn_name}({fn_args})")

                fn = available_functions.get(fn_name)
                if fn:
                    result = fn(**fn_args)
                else:
                    result = {"error": f"Unknown function: {fn_name}"}

                # Feed the tool result back to the model
                history.append(item)
                history.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(result),
                })

        if not has_function_call:
            break

        # Make a follow-up call so the model can respond with text
        response = client.responses.create(
            model="gpt-4o-mini",
            input=history,
            tools=tools
        )

    # Print the final text output
    if response.output_text:
        print(f"Assistant: {response.output_text}")

    history.append({
        "role": "assistant",
        "content": response.output_text
    })