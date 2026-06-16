import pytest
import requests
from utils.helpers import BASE_URL, criar_usuario, gerar_email
from jsonschema import validate
from schemas.login_schema import LOGIN_SUCESSO_SCHEMA

@pytest.mark.login
def test_deve_realizar_login_com_sucesso():
    usuario = criar_usuario()
    payload = {
        "email": usuario["email"],
        "password": usuario["password"]
    }
    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )
    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=LOGIN_SUCESSO_SCHEMA)
    assert body["message"] == "Login realizado com sucesso"
    assert "authorization" in body

@pytest.mark.login
def test_nao_deve_realizar_login_com_credenciais_invalidas():
    usuario = criar_usuario()
    payload = {
        "email": usuario["email"],
        "password": "senha_incorreta"
    }
    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )
    assert response.status_code == 401
    body = response.json()
    assert body["message"] == "Email e/ou senha inválidos"

@pytest.mark.login
def test_nao_deve_realizar_login_com_email_inexistente():
    payload = {
        "email": gerar_email(),
        "password": "senha123"
    }
    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )
    assert response.status_code == 401
    body = response.json()
    assert body["message"] == "Email e/ou senha inválidos"

@pytest.mark.login
def test_nao_deve_realizar_login_com_email_vazio():
    payload = {
        "email": "",
        "password": "teste123"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400
    body = response.json()
    assert "email" in body

@pytest.mark.login
def test_nao_deve_realizar_login_com_senha_vazia():
    payload = {
        "email": "teste@teste.com",
        "password": ""
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400
    body = response.json()
    assert "password" in body

@pytest.mark.login
def test_nao_deve_realizar_login_com_campos_vazios():
    payload = {
        "email": "",
        "password": ""
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400
    body = response.json()
    assert "email" in body
    assert "password" in body