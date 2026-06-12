# Desafio Semana 3 - Testes Automatizados de API (ServeRest)

Projeto desenvolvido para o desafio da Semana 3 utilizando Python, Pytest e Requests para automatizar testes do endpoint de usuários da API ServeRest.

## API utilizada

https://compassuol.serverest.dev

## Tecnologias

* Python 3.14
* Pytest
* Requests
* UUID

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd desafio-serverest
```

Crie e ative o ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução dos testes

Executar todos os testes:

```bash
pytest -v
```

Executar com logs detalhados:

```bash
pytest -v -s
```

## Cenários testados

### Usuários

* Listar usuários
* Cadastrar usuário com sucesso
* Cadastrar usuário com e-mail duplicado
* Cadastrar usuário sem nome
* Cadastrar usuário sem e-mail
* Cadastrar usuário sem senha
* Cadastrar usuário sem campo administrador
* Buscar usuário por ID
* Buscar usuário inexistente
* Atualizar usuário
* Excluir usuário

## Estratégia adotada

* Testes independentes entre si
* Utilização de e-mails dinâmicos para evitar conflitos
* Validação de status codes
* Validação da estrutura das respostas JSON
* Cobertura de cenários positivos e negativos

## Endpoints testados

```http
GET    /usuarios
POST   /usuarios
GET    /usuarios/{id}
PUT    /usuarios/{id}
DELETE /usuarios/{id}
```

## Resultados

Projeto contendo 11 testes automatizados cobrindo os cenários mínimos solicitados no desafio.

## Autor

Rayane Duarte
