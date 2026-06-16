import pytest
import requests

from utils.helpers import BASE_URL

@pytest.mark.carrinhos
def test_deve_listar_carrinhos_com_sucesso():
    response = requests.get(f"{BASE_URL}/carrinhos")
    assert response.status_code == 200
    body = response.json()
    assert "quantidade" in body
    assert "carrinhos" in body
    assert isinstance(body["carrinhos"], list)

@pytest.mark.carrinhos
def test_deve_buscar_carrinho_por_id_com_sucesso():
    carrinhos = requests.get(f"{BASE_URL}/carrinhos")
    assert carrinhos.status_code == 200
    lista_carrinhos = carrinhos.json()["carrinhos"]
    if not lista_carrinhos:
        pytest.skip("Não existem carrinhos disponíveis para busca por ID")
    carrinho_id = lista_carrinhos[0]["_id"]
    response = requests.get(f"{BASE_URL}/carrinhos/{carrinho_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["_id"] == carrinho_id
    assert "produtos" in body
    assert "precoTotal" in body
    assert "quantidadeTotal" in body
    assert "idUsuario" in body

@pytest.mark.carrinhos
def test_deve_retornar_erro_ao_buscar_carrinho_inexistente():
    carrinho_id_inexistente = "0000000000000000"
    response = requests.get(f"{BASE_URL}/carrinhos/{carrinho_id_inexistente}")
    assert response.status_code == 400
    body = response.json()
    assert body["message"] == "Carrinho não encontrado"

@pytest.mark.carrinhos
def test_deve_retornar_erro_ao_buscar_carrinho_com_id_invalido():
    carrinho_id_invalido = "123"
    response = requests.get(f"{BASE_URL}/carrinhos/{carrinho_id_invalido}")
    assert response.status_code == 400
    body = response.json()
    assert body["id"] == "id deve ter exatamente 16 caracteres alfanuméricos"

@pytest.mark.carrinhos
def test_deve_cadastrar_carrinho_com_sucesso(admin_headers):
    produtos = requests.get(f"{BASE_URL}/produtos")
    assert produtos.status_code == 200
    produto_id = produtos.json()["produtos"][0]["_id"]
    payload = {
        "produtos": [
            {
                "idProduto": produto_id,
                "quantidade": 1
            }
        ]
    }
    response = requests.post(
        f"{BASE_URL}/carrinhos",
        json=payload,
        headers=admin_headers
    )
    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"

@pytest.mark.carrinhos
def test_nao_deve_cadastrar_mais_de_um_carrinho_por_usuario(admin_headers):
    produtos = requests.get(f"{BASE_URL}/produtos")
    assert produtos.status_code == 200
    produto_id = produtos.json()["produtos"][0]["_id"]
    payload = {
        "produtos": [
            {
                "idProduto": produto_id,
                "quantidade": 1
            }
        ]
    }
    primeira_response = requests.post(
        f"{BASE_URL}/carrinhos",
        json=payload,
        headers=admin_headers
    )
    assert primeira_response.status_code == 201
    segunda_response = requests.post(
        f"{BASE_URL}/carrinhos",
        json=payload,
        headers=admin_headers
    )
    assert segunda_response.status_code == 400
    body = segunda_response.json()
    assert body["message"] == "Não é permitido ter mais de 1 carrinho"