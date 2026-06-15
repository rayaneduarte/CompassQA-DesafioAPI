import uuid
import requests

BASE_URL = "https://compassuol.serverest.dev"


def gerar_email():
    return f"rayane_{uuid.uuid4().hex[:8]}@teste.com"


def gerar_usuario(administrador="true"):
    return {
        "nome": "Rayane QA",
        "email": gerar_email(),
        "password": "teste123",
        "administrador": administrador
    }


def criar_usuario(administrador="true"):
    usuario = gerar_usuario(administrador)
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 201
    usuario["_id"] = response.json()["_id"]
    return usuario


def obter_token_admin():
    usuario = criar_usuario(administrador="true")
    payload = {
        "email": usuario["email"],
        "password": usuario["password"]
    }

    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    return response.json()["authorization"]