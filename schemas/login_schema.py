LOGIN_SUCESSO_SCHEMA = {
    "type": "object",
    "required": ["message", "authorization"],
    "properties": {
        "message": {"type": "string"},
        "authorization": {"type": "string"}
    }
}