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

    reply = assistant.chat(user_input)

    print_copilot_block(reply)
