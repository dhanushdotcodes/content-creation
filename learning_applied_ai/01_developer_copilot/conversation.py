class Conversation:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append({
            "type": "user",
            "content": message
        })

    def add_tool_message(self, tool_name, message):
        self.history.append({
            "type": "tool",
            "content": message
        })

    def add_assistant_message(self, message):
        self.history.append({
            "type": "assistant",
            "content": message
        })

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
