from openai import OpenAI
from prompts.system_prompts import IMPROVE_CODE_PROMPT


def improve_code(code: str) -> str:
    """
    Rewrites and improves the provided code, then summarizes the changes.
    """
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=IMPROVE_CODE_PROMPT,
        input=code,
    )
    return response.output_text
