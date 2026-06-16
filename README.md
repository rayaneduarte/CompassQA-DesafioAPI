# Desafio Bootcamp - Testes Automatizados de API (ServeRest)

Projeto desenvolvido utilizando Python, Pytest e Requests para automatizar testes da API ServeRest, cobrindo os endpoints de Usuários, Login, Produtos e cenários adicionais para Carrinhos.

## API utilizada

https://compassuol.serverest.dev

## Tecnologias

* Python 3.14.5
* Pytest
* Requests
* UUID
* Git e GitHub
* GitHub Actions
* jsonschema

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

Executar toda a suíte:

```bash
python -m pytest -v
```

Executar com logs detalhados:

```bash
python -m pytest -v -s
```

Executar apenas os testes de usuários:

```bash
python -m pytest -m usuarios
```

Executar apenas os testes de login:

```bash
python -m pytest -m login
```

Executar apenas os testes de produtos:

```bash
python -m pytest -m produtos
```

Executar apenas os testes de carrinhos:

```bash
python -m pytest -m carrinhos
```

## Estrutura do Projeto

```text
CompassQA/
│
├── tests/
│   ├── conftest.py
│   ├── test_usuarios.py
│   ├── test_login.py
│   ├── test_produtos.py
│   └── test_carrinhos.py
│
├── schemas/
│   ├── usuario_schema.py
│   ├── login_schema.py
│   └── produto_schema.py
│
├── utils/
│   └── helpers.py
│
├── PLANO-DE-TESTES.md
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

## Endpoints Testados

### Usuários

```http
GET    /usuarios
POST   /usuarios
GET    /usuarios/{id}
PUT    /usuarios/{id}
DELETE /usuarios/{id}
```

### Login

```http
POST   /login
```

### Produtos

```http
GET    /produtos
POST   /produtos
GET    /produtos/{id}
PUT    /produtos/{id}
DELETE /produtos/{id}
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

### Login

* Login com credenciais válidas
* Login com senha incorreta
* Login com e-mail inexistente
* Login com e-mail vazio
* Login com senha vazia
* Login com campos vazios

### Produtos

* Listar produtos
* Buscar produto por ID válido
* Buscar produto inexistente
* Cadastrar produto com administrador
* Cadastrar produto sem token
* Cadastrar produto com usuário comum
* Cadastrar produto com dados inválidos
* Atualizar produto existente
* Excluir produto existente
* Excluir produto inexistente

### Cenários Adicionais

* Buscar usuário com ID inválido
* Buscar produto com ID inválido
* Verificação de comportamento ao atualizar produto inexistente

## Estratégia Adotada

* Testes independentes entre si
* Uso de UUID para geração de dados dinâmicos
* Cobertura de cenários positivos e negativos
* Validação de status codes
* Validação da estrutura das respostas JSON
* Utilização de helpers para reutilização de código
* Utilização de fixtures para autenticação e configuração compartilhada
* Validação da estrutura das respostas utilizando JSON Schema

## Cobertura de Testes

### Método de Cálculo

A cobertura foi calculada com base nos cenários definidos no Plano de Testes.

Fórmula utilizada:

```text
Cobertura (%) = (Cenários Implementados / Cenários Planejados) × 100
```

### Resultado

| Endpoint | Planejados | Implementados | Cobertura |
| -------- | ---------- | ------------- | --------- |
| Usuários | 11         | 11            | 100%      |
| Login    | 6          | 6             | 100%      |
| Produtos | 10         | 10            | 100%      |

**Cobertura Total:** 27 de 27 cenários planejados implementados (**100%**)

### Testes Adicionais

Além dos cenários previstos no Plano de Testes, foram implementados:

* Buscar usuário com ID inválido
* Buscar produto com ID inválido
* Investigação do comportamento de atualização de produto inexistente
* Implementação de testes exploratórios para o endpoint de carrinhos

**Total geral da suíte:** 36 testes automatizados.

### Carrinhos (Extra)

Foram implementados testes exploratórios para o endpoint de carrinhos:

* Listar carrinhos
* Buscar carrinho por ID
* Buscar carrinho inexistente
* Buscar carrinho com ID inválido
* Cadastrar carrinho com sucesso
* Não permitir mais de um carrinho por usuário

### Cenários Fora do Escopo

* Testes de performance
* Testes de carga
* Testes de segurança
* Testes de interface gráfica
* Testes de acessibilidade
* Integrações externas

## Bug Report

Durante a execução da suíte foi identificado um comportamento inesperado no endpoint:

```http
PUT /produtos/{id}
```

Quando um ID inexistente é informado, a API cria um novo produto ao invés de retornar uma mensagem informando que o produto não foi encontrado.

O bug foi documentado na Issue #2 do repositório.

## Integração Contínua

O projeto utiliza GitHub Actions para execução automática dos testes a cada push e pull request.
A execução é realizada em etapas separadas para reduzir impactos de instabilidade da API utilizada nos testes.

A pipeline realiza:

- Configuração do ambiente Python
- Instalação das dependências
- Execução automática da suíte de testes com Pytest

## Validação de JSON Schema

Foram implementadas validações de estrutura das respostas utilizando JSON Schema nos seguintes endpoints:

* GET /usuarios
* POST /login
* GET /produtos

As validações garantem que os contratos esperados da API sejam mantidos, verificando tipos de dados, campos obrigatórios e estrutura das respostas.
Essa abordagem complementa as validações de status code e regras de negócio realizadas pelos testes funcionais.

## Autor

Rayane Duarte
