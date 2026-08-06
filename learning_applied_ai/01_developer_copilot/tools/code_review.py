from openai import OpenAI
from prompts.system_prompts import CODE_REVIEW_PROMPT


def code_review(code: str) -> str:
    """
    Reviews the provided code and returns detailed feedback.
    """
    client = OpenAI()
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=CODE_REVIEW_PROMPT,
        input=code,
    )
    return response.output_text
