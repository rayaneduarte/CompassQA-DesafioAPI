# Desafio Semana 3 - Testes Automatizados de API (ServeRest)

Projeto desenvolvido para o desafio da Semana 3 utilizando Python, Pytest e Requests para automatizar testes do endpoint de usuários da API ServeRest.

## API utilizada

https://compassuol.serverest.dev

## Tecnologias

* Python 3.10+
* Pytest
* Requests
* UUID (geração de e-mails únicos para os testes)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/rayaneduarte/CompassQA-DesafioAPI.git
```

Acesse a pasta do projeto:

```bash
cd CompassQA-DesafioAPI
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

## Estrutura do Projeto

```text
CompassQA-DesafioAPI/
│
├── tests/
│   └── test_usuarios.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

## Cenários Testados

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

## Estratégia Adotada

* Testes independentes entre si
* Utilização de UUID para geração de e-mails únicos, evitando conflitos entre execuções
* Validação de status codes das respostas HTTP
* Validação da estrutura dos dados retornados pela API
* Cobertura de cenários positivos e negativos
* Utilização de funções auxiliares para reduzir duplicação de código

## Endpoints Testados

```http
GET    /usuarios
POST   /usuarios
GET    /usuarios/{id}
PUT    /usuarios/{id}
DELETE /usuarios/{id}
```

## Validações Realizadas

Os testes validam:

* Status codes esperados para cada cenário
* Estrutura das respostas JSON
* Mensagens de sucesso e erro retornadas pela API
* Integridade dos dados cadastrados e consultados
* Comportamento esperado para dados inválidos ou inexistentes

## Resultados

Projeto contendo 11 testes automatizados para o endpoint de usuários da API ServeRest, cobrindo os cenários mínimos propostos no desafio e cenários adicionais de validação.

## Autor

Rayane Duarte
