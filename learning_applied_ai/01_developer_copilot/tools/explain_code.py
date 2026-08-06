from openai import OpenAI
from prompts.system_prompts import EXPLAIN_CODE_PROMPT


def explain_code(code: str) -> str:
    """
    Explains what the provided code does in plain language.
    """
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=EXPLAIN_CODE_PROMPT,
        input=code,
    )
    return response.output_text
