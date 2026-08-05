tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Returns current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name, e.g., London or Tokyo",
                },
            },
            "required": ["city"],
        },
    },
    {
        "type": "function",
        "name": "get_random_joke",
        "description": "Returns a random joke.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "type": "function",
        "name": "get_current_time",
        "description": "Returns current time for a given timezone.",
        "parameters": {
            "type": "object",
            "properties": {
                "timezone": {
                    "type": "string",
                    "description": "The IANA timezone name, e.g., Asia/Kolkata, Europe/London, America/New_York",
                },
            },
            "required": ["timezone"],
        },
    },
    {
        "type": "function",
        "name": "currency_convertor",
        "description": "Converts currency using Frankfurter API.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The amount to convert",
                },
                "from_currency": {
                    "type": "string",
                    "description": "The source currency code, e.g., USD, EUR, INR",
                },
                "to_currency": {
                    "type": "string",
                    "description": "The target currency code, e.g., EUR, USD, GBP",
                },
            },
            "required": ["amount", "from_currency", "to_currency"],
        },
    },
]