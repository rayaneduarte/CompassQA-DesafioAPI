LISTAR_PRODUTOS_SCHEMA = {
    "type": "object",
    "required": ["quantidade", "produtos"],
    "properties": {
        "quantidade": {"type": "integer"},
        "produtos": {"type": "array"}
    }
}

CADASTRAR_PRODUTO_SCHEMA = {
    "type": "object",
    "required": ["message", "_id"],
    "properties": {
        "message": {"type": "string"},
        "_id": {"type": "string"}
    }
}