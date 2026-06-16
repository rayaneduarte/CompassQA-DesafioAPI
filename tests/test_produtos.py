import pytest
import requests
from utils.helpers import BASE_URL, gerar_produto, criar_usuario
from jsonschema import validate
from schemas.produto_schema import LISTAR_PRODUTOS_SCHEMA, CADASTRAR_PRODUTO_SCHEMA

@pytest.mark.produtos
def test_deve_listar_produtos_com_sucesso():
    response = requests.get(f"{BASE_URL}/produtos")
    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=LISTAR_PRODUTOS_SCHEMA)
    assert "quantidade" in body
    assert "produtos" in body
    assert isinstance(body["produtos"], list)

@pytest.mark.produtos
def test_deve_buscar_produto_por_id_com_sucesso():
    produtos = requests.get(f"{BASE_URL}/produtos")
    produto_id = produtos.json()["produtos"][0]["_id"]
    response = requests.get(f"{BASE_URL}/produtos/{produto_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["_id"] == produto_id
    assert "nome" in body
    assert "preco" in body
    assert "descricao" in body
    assert "quantidade" in body

@pytest.mark.produtos
def test_deve_retornar_erro_ao_buscar_produto_inexistente():
    produto_id_inexistente = "0000000000000000"
    response = requests.get(
        f"{BASE_URL}/produtos/{produto_id_inexistente}"
    )
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Produto não encontrado"

@pytest.mark.produtos
def test_deve_cadastrar_produto_com_sucesso(admin_headers):
    produto = gerar_produto()
    headers = admin_headers
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto,
        headers=headers
    )
    assert response.status_code == 201
    body = response.json()
    validate(instance=body, schema=CADASTRAR_PRODUTO_SCHEMA)
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

@pytest.mark.produtos
def test_nao_deve_cadastrar_produto_sem_token():
    produto = gerar_produto()
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto
    )
    assert response.status_code == 401
    body = response.json()
    assert "Token de acesso" in body["message"]

@pytest.mark.produtos
def test_nao_deve_cadastrar_produto_com_usuario_comum():
    usuario = criar_usuario(administrador="false")
    login = requests.post( 
        f"{BASE_URL}/login",
        json={
            "email": usuario["email"],
            "password": usuario["password"]
        }
    )
    assert login.status_code == 200
    token = login.json()["authorization"]
    produto = gerar_produto()
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto,
        headers={
            "Authorization": token
        }
    )
    assert response.status_code == 403
    body = response.json()
    assert body["message"] == "Rota exclusiva para administradores"

@pytest.mark.produtos
def test_nao_deve_cadastrar_produto_com_dados_invalidos(admin_headers):
    produto = gerar_produto()
    produto.pop("nome")
    response = requests.post(
        f"{BASE_URL}/produtos",
        json=produto,
        headers=admin_headers
    )
    assert response.status_code == 400
    body = response.json()
    assert "nome" in body

@pytest.mark.produtos
def test_deve_atualizar_produto_existente_com_sucesso(admin_headers):
    produto = gerar_produto()
    cadastro = requests.post(
        f"{BASE_URL}/produtos",
        json=produto,
        headers=admin_headers
    )
    produto_id = cadastro.json()["_id"]
    produto_atualizado = gerar_produto()
    response = requests.put(
        f"{BASE_URL}/produtos/{produto_id}",
        json=produto_atualizado,
        headers=admin_headers
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Registro alterado com sucesso"

@pytest.mark.produtos
def test_deve_excluir_produto_existente_com_sucesso(admin_headers):
    produto = gerar_produto()
    cadastro = requests.post(
        f"{BASE_URL}/produtos",
        json=produto,
        headers=admin_headers
    )
    produto_id = cadastro.json()["_id"]
    response = requests.delete(
        f"{BASE_URL}/produtos/{produto_id}",
        headers=admin_headers
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Registro excluído com sucesso"

@pytest.mark.produtos
def test_deve_retornar_erro_ao_excluir_produto_inexistente(admin_headers):
    produto_id_inexistente = "0000000000000000"
    response = requests.delete(
        f"{BASE_URL}/produtos/{produto_id_inexistente}",
        headers=admin_headers
    )
    assert response.status_code == 200
    body = response.json()
    assert body["message"] == "Nenhum registro excluído"

@pytest.mark.produtos
def test_comportamento_inesperado_ao_atualizar_produto_inexistente(admin_headers):
    produto = gerar_produto()
    response = requests.put(
        f"{BASE_URL}/produtos/0000000000000000",
        json=produto,
        headers=admin_headers
    )
    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body

@pytest.mark.produtos
def test_deve_retornar_erro_ao_buscar_produto_com_id_invalido():
    produto_id_invalido = "123"
    response = requests.get(
        f"{BASE_URL}/produtos/{produto_id_invalido}"
    )
    assert response.status_code == 400
    body = response.json()
    assert body["id"] == "id deve ter exatamente 16 caracteres alfanuméricos"