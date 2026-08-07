class Conversation:
    def __init__(self, system_prompt: str):
        self.history = [
            {"role": "system", "content": system_prompt}
        ]

    def add_user_message(self, message: str):
        self.history.append({"role": "user", "content": message})

    def add_function_call(self, item):
        """Store the raw function_call item the model emitted."""
        # Normalize the function_call item into a plain dict so the
        # conversation history contains only serializable structures.
        name = getattr(item, "name", None) or (item.get("name") if isinstance(item, dict) else None)
        arguments = getattr(item, "arguments", None) or (item.get("arguments") if isinstance(item, dict) else None)
        call_id = getattr(item, "call_id", None) or (item.get("call_id") if isinstance(item, dict) else None)

        self.history.append({
            "type": "function_call",
            "name": name,
            "arguments": arguments,
            "call_id": call_id,
        })

    def add_tool_result(self, call_id: str, output: str):
        self.history.append({
            "type": "function_call_output",
            "call_id": call_id,
            "output": output,
        })

    def add_assistant_message(self, message: str):
        self.history.append({"role": "assistant", "content": message})

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = [self.history[0]]  # keep the system prompt
