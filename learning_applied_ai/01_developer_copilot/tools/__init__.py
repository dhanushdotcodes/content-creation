from tools.code_review import code_review
from tools.explain_code import explain_code
from tools.improve_code import improve_code

# OpenAI tool definitions
tool_definitions = [
    {
        "type": "function",
        "name": "explain_code",
        "description": "Explains what a piece of code does in plain language, walking through the logic step by step.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The source code to explain.",
                },
            },
            "required": ["code"],
        },
    },
    {
        "type": "function",
        "name": "code_review",
        "description": "Reviews code for bugs, quality issues, security problems, and best-practice violations.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The source code to review.",
                },
            },
            "required": ["code"],
        },
    },
    {
        "type": "function",
        "name": "improve_code",
        "description": "Refactors and improves code quality, fixing bugs and applying clean-code principles.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "string",
                    "description": "The source code to improve.",
                },
            },
            "required": ["code"],
        },
    },
]

# Map tool names to callable functions
available_functions = {
    "explain_code": explain_code,
    "code_review": code_review,
    "improve_code": improve_code,
}
