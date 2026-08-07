import json

from openai import OpenAI
from dotenv import load_dotenv

from conversation import Conversation
from tools import tool_definitions, available_functions
from prompts.system_prompts import DEVELOPER_COPILOT_PROMPT

load_dotenv()

class Assistant:
    def __init__(self):
        self.client = OpenAI()
        self.conversation = Conversation(system_prompt=DEVELOPER_COPILOT_PROMPT)

    def chat(self, user_input: str) -> str:
        self.conversation.add_user_message(user_input)

        response = self._call_llm()

        # Tool-call loop — keep going until the model gives a plain text response
        while response.output:
            has_tool_call = False

            for item in response.output:
                if item.type == "function_call":
                    has_tool_call = True
                    self.conversation.add_function_call(item)
                    result = self._execute_tool(item.name, item.arguments)
                    self.conversation.add_tool_result(
                        call_id=item.call_id,
                        output=json.dumps(result),
                    )

            if not has_tool_call:
                break

            response = self._call_llm()

        assistant_reply = response.output_text or ""
        self.conversation.add_assistant_message(assistant_reply)
        return assistant_reply

    def _call_llm(self):
        return self.client.responses.create(
            model="gpt-4o-mini",
            input=self.conversation.get_history(),
            tools=tool_definitions,
        )

    def _execute_tool(self, tool_name: str, arguments: str) -> str:
        fn = available_functions.get(tool_name)
        if fn is None:
            return json.dumps({"error": f"Unknown tool: {tool_name}"})
        # The `arguments` value may be a JSON string or an already-parsed dict
        # depending on the SDK/response shape. Handle both safely.
        if isinstance(arguments, str):
            try:
                fn_args = json.loads(arguments)
            except json.JSONDecodeError:
                # If it's a raw string (not JSON), many tools expect a
                # single `code` parameter; wrap it accordingly.
                fn_args = {"code": arguments}
        elif isinstance(arguments, dict):
            fn_args = arguments
        else:
            # Fallback: pass through as-is; the tool can validate further.
            fn_args = arguments

        # If the tool expects a single `code` param but we received a string,
        # ensure we call it with the correct signature.
        if isinstance(fn_args, dict):
            return fn(**fn_args)
        return fn(fn_args)
