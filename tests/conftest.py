import pytest

from utils.helpers import obter_token_admin

@pytest.fixture() #Criei uma fixture para obter o token de admin, assim posso reutilizar em outros testes que necessitem de autenticação
def token_admin():
    return obter_token_admin()

@pytest.fixture
def admin_headers(token_admin):
    return {
        "Authorization": token_admin
    }