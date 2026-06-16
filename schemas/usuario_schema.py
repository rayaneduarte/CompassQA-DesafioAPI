LISTAR_USUARIOS_SCHEMA = {
    "type": "object",
    "required": ["quantidade", "usuarios"],
    "properties": {
        "quantidade": {"type": "integer"},
        "usuarios": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["nome", "email", "password", "administrador", "_id"],
                "properties": {
                    "nome": {"type": "string"},
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                    "administrador": {"type": "string"},
                    "_id": {"type": "string"}
                }
            }
        }
    }
}