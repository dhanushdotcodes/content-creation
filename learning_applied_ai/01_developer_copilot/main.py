import sys
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv
from assistant import Assistant

load_dotenv()

# ── helpers ───────────────────────────────────────────────────────────────────

def term_width() -> int:
    return shutil.get_terminal_size(fallback=(80, 24)).columns

def divider(char: str = "─") -> str:
    return char * term_width()

def print_banner():
    width = term_width()
    title   = "🤖  Developer Copilot"
    subtitle = "explain · review · improve your code"
    hint    = "type  exit  or  quit  to stop"
    print()
    print(divider("═"))
    print(title.center(width))
    print(subtitle.center(width))
    print(divider("═"))
    print(hint.center(width))
    print()

def print_user_block(text: str):
    width = term_width()
    print()
    print(f"  YOU")
    print(f"  {divider('·')[:width - 2]}")
    for line in text.splitlines():
        print(f"  {line}")
    print()

def print_tool_call(name: str):
    print(f"  ⚙  {name}(…) — thinking…")

def print_copilot_block(text: str):
    width = term_width()
    print(divider("─"))
    print(f"  COPILOT")
    print(f"  {divider('·')[:width - 2]}")
    for line in text.splitlines():
        print(f"  {line}")
    print()
    print(divider("─"))
    print()

# ── main loop ─────────────────────────────────────────────────────────────────

assistant = Assistant()

def _chat_with_ui(user_input: str) -> str:
    import json

    assistant.conversation.add_user_message(user_input)
    response = assistant._call_llm()

    while response.output:
        has_tool_call = False
        for item in response.output:
            if item.type == "function_call":
                has_tool_call = True
                # The API requires the function_call item itself in history
                # before its matching function_call_output
                assistant.conversation.add_function_call(item)
                print_tool_call(item.name)
                result = assistant._execute_tool(item.name, item.arguments)
                assistant.conversation.add_tool_result(
                    call_id=item.call_id,
                    output=json.dumps(result),
                )
        if not has_tool_call:
            break
        response = assistant._call_llm()

    reply = response.output_text or ""
    assistant.conversation.add_assistant_message(reply)
    return reply


print_banner()

while True:
    try:
        user_input = input("  → ").strip()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{divider()}\n  Goodbye!\n{divider()}\n")
        break

    if not user_input:
        continue

    if user_input.lower() in {"exit", "quit"}:
        print(f"\n{divider()}\n  Goodbye!\n{divider()}\n")
        break

    print_user_block(user_input)

    reply = _chat_with_ui(user_input)

    print_copilot_block(reply)
