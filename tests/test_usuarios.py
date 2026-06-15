import pytest
import requests

from utils.helpers import BASE_URL, gerar_email, gerar_usuario

@pytest.mark.usuarios
def test_deve_listar_usuarios_com_sucesso():
    response = requests.get(f"{BASE_URL}/usuarios")
    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "usuarios" in body
    assert isinstance(body["usuarios"], list)


@pytest.mark.usuarios
def test_deve_cadastrar_usuario_com_sucesso():
    usuario = gerar_usuario()
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body


@pytest.mark.usuarios
def test_nao_deve_cadastrar_usuario_com_email_duplicado():
    usuario = gerar_usuario()
    requests.post(f"{BASE_URL}/usuarios", json=usuario)
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Este email já está sendo usado"


@pytest.mark.usuarios
def test_nao_deve_cadastrar_usuario_sem_nome():
    usuario = gerar_usuario()
    usuario.pop("nome")
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 400
    body = response.json()
    assert "nome" in body


@pytest.mark.usuarios
def test_nao_deve_cadastrar_usuario_sem_email():
    usuario = gerar_usuario()
    usuario.pop("email")
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 400
    body = response.json()
    assert "email" in body


@pytest.mark.usuarios
def test_nao_deve_cadastrar_usuario_sem_password():
    usuario = gerar_usuario()
    usuario.pop("password")
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 400
    body = response.json()
    assert "password" in body


@pytest.mark.usuarios
def test_nao_deve_cadastrar_usuario_sem_administrador():
    usuario = gerar_usuario()
    usuario.pop("administrador")
    response = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    assert response.status_code == 400
    body = response.json()
    assert "administrador" in body


@pytest.mark.usuarios
def test_deve_buscar_usuario_por_id():
    usuario = gerar_usuario()
    cadastro = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    user_id = cadastro.json()["_id"]
    response = requests.get(f"{BASE_URL}/usuarios/{user_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["_id"] == user_id
    assert body["nome"] == usuario["nome"]
    assert body["email"] == usuario["email"]
    assert body["password"] == usuario["password"]
    assert body["administrador"] == usuario["administrador"]


@pytest.mark.usuarios
def test_deve_retornar_erro_ao_buscar_usuario_inexistente():
    user_id_inexistente = "0000000000000000"
    response = requests.get(f"{BASE_URL}/usuarios/{user_id_inexistente}")
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Usuário não encontrado"


@pytest.mark.usuarios
def test_deve_atualizar_usuario_com_sucesso():
    usuario = gerar_usuario()
    cadastro = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    user_id = cadastro.json()["_id"]
    usuario_atualizado = {
        "nome": "Rayane QA Atualizada",
        "email": gerar_email(),
        "password": "novaSenha123",
        "administrador": "false"
    }

    response = requests.put(f"{BASE_URL}/usuarios/{user_id}", json=usuario_atualizado)
    assert response.status_code == 200
    body = response.json()
    assert "message" in body
    assert body["message"] == "Registro alterado com sucesso"


@pytest.mark.usuarios
def test_deve_excluir_usuario_com_sucesso():
    usuario = gerar_usuario()
    cadastro = requests.post(f"{BASE_URL}/usuarios", json=usuario)
    user_id = cadastro.json()["_id"]
    response = requests.delete(f"{BASE_URL}/usuarios/{user_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Registro excluído com sucesso"