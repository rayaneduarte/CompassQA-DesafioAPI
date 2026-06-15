# Plano de Testes - API ServeRest

## 1. Objetivo

Garantir a qualidade e confiabilidade da API ServeRest através de testes automatizados de API, validando o comportamento funcional dos endpoints de Usuários, Login e Produtos, assegurando que as respostas da API atendam aos requisitos de negócio e especificações técnicas.

## 2. Escopo

### 2.1 Funcionalidades Cobertas

#### **Usuários** ✓ (Implementado)
- Listagem de usuários
- Cadastro de usuários (cenários positivos e negativos)
- Validação de campos obrigatórios
- Validação de e-mail duplicado
- Busca de usuário por ID
- Atualização de usuários
- Exclusão de usuários

#### **Login** (Planejado)
- Autenticação com credenciais válidas
- Validação de senha incorreta
- Validação de e-mail inexistente
- Validação de campos obrigatórios

#### **Produtos** (Planejado)
- Listagem de produtos
- Busca de produto por ID
- Cadastro de produtos (com autorização)
- Validação de autorização (token de administrador)
- Atualização de produtos
- Exclusão de produtos

### 2.2 Funcionalidades Fora do Escopo

- Testes de performance e carga
- Testes de segurança (penetração, vulnerabilidades)
- Validação de infraestrutura e disponibilidade
- Testes de interface gráfica (UI)
- Testes de integração com sistemas externos
- Testes de acessibilidade
- Validação de logs e monitoramento

## 3. Estratégia de Testes

### 3.1 Abordagem

- **Testes Funcionais End-to-End**: Validação do comportamento completo dos endpoints
- **Testes de Contrato**: Verificação da estrutura das respostas (status code, schema)
- **Testes de Validação**: Verificação de regras de negócio e validações de entrada
- **Testes de Cenários Negativos**: Validação de tratamento de erros e exceções

### 3.2 Níveis de Teste

- **Teste de API**: Camada principal de automação
- **Teste de Integração**: Validação do fluxo entre endpoints (ex: criar usuário → fazer login → criar produto)

### 3.3 Técnicas Aplicadas

- **Particionamento de Equivalência**: Agrupamento de dados de entrada válidos e inválidos
- **Testes Baseados em Estado**: Validação de transições (usuário não autenticado → autenticado)
- **Geração Dinâmica de Dados**: Uso de UUID para garantir independência entre testes

## 4. Cenários de Teste

### 4.1 Endpoint: Usuários (Status: ✓ Implementado)

| ID | Cenário | Prioridade | Status |
|----|---------|------------|--------|
| US-01 | Listar todos os usuários | Alta | ✓ |
| US-02 | Cadastrar usuário com dados válidos | Alta | ✓ |
| US-03 | Cadastrar usuário com e-mail duplicado | Alta | ✓ |
| US-04 | Cadastrar usuário sem nome | Média | ✓ |
| US-05 | Cadastrar usuário sem e-mail | Média | ✓ |
| US-06 | Cadastrar usuário sem senha | Média | ✓ |
| US-07 | Cadastrar usuário sem campo administrador | Média | ✓ |
| US-08 | Buscar usuário por ID válido | Alta | ✓ |
| US-09 | Buscar usuário com ID inexistente | Média | ✓ |
| US-10 | Atualizar usuário existente | Alta | ✓ |
| US-11 | Excluir usuário existente | Alta | ✓ |

**Cobertura atual: 11 cenários**

---

### 4.2 Endpoint: Login (Status: Planejado)

| ID | Cenário | Entrada | Resultado Esperado | Prioridade |
|----|---------|---------|-------------------|------------|
| LG-01 | Login com credenciais válidas | E-mail e senha válidos | Status 200, token retornado | Alta |
| LG-02 | Login com senha incorreta | E-mail válido, senha inválida | Status 401, mensagem de erro | Alta |
| LG-03 | Login com e-mail inexistente | E-mail não cadastrado | Status 401, mensagem de erro | Alta |
| LG-04 | Login com campo e-mail vazio | E-mail vazio, senha válida | Status 400, mensagem de validação | Média |
| LG-05 | Login com campo senha vazio | E-mail válido, senha vazia | Status 400, mensagem de validação | Média |
| LG-06 | Login com ambos os campos vazios | E-mail e senha vazios | Status 400, mensagem de validação | Média |

**Cobertura planejada: 6 cenários**

**Critérios de Aceitação:**
- Token JWT deve ser retornado em login bem-sucedido
- Token deve ser válido para requisições autenticadas
- Mensagens de erro devem ser descritivas e consistentes

---

### 4.3 Endpoint: Produtos (Status: Planejado)

| ID | Cenário | Pré-condição | Resultado Esperado | Prioridade |
|----|---------|--------------|-------------------|------------|
| PR-01 | Listar todos os produtos | Nenhuma | Status 200, lista de produtos | Alta |
| PR-02 | Buscar produto por ID válido | Produto cadastrado | Status 200, dados do produto | Alta |
| PR-03 | Buscar produto com ID inexistente | - | Status 400, mensagem de erro | Média |
| PR-04 | Cadastrar produto como administrador | Token de admin válido | Status 201, produto criado | Alta |
| PR-05 | Cadastrar produto sem token | Sem autenticação | Status 401, acesso negado | Alta |
| PR-06 | Cadastrar produto como usuário comum | Token de usuário não-admin | Status 403, acesso negado | Alta |
| PR-07 | Cadastrar produto com dados inválidos | Token válido, dados incompletos | Status 400, mensagens de validação | Média |
| PR-08 | Atualizar produto existente | Token de admin, produto existente | Status 200, produto atualizado | Alta |
| PR-09 | Excluir produto existente | Token de admin, produto existente | Status 200, produto excluído | Alta |
| PR-10 | Excluir produto inexistente | Token de admin, ID inválido | Status 200, mensagem apropriada | Baixa |

**Cobertura planejada: 10 cenários**

**Critérios de Aceitação:**
- Apenas administradores podem cadastrar, atualizar e excluir produtos
- Validação de autorização deve ocorrer antes da validação de dados
- Produtos devem ter nome único

---

## 5. Critérios de Qualidade

### 5.1 Critérios de Aceitação dos Testes

- ✅ Teste deve ser independente (não depender de outros testes)
- ✅ Teste deve ser repetível (mesmo resultado em múltiplas execuções)
- ✅ Dados dinâmicos devem ser gerados automaticamente (UUID)
- ✅ Assertions devem validar status code, estrutura e conteúdo da resposta
- ✅ Mensagens de erro devem ser claras e assertivas
- ✅ Tempo de resposta deve ser razoável (< 3 segundos por requisição)

### 5.2 Padrões de Código

- Nomenclatura descritiva de testes (padrão: `test_<ação>_<resultado_esperado>`)
- Uso de fixtures para setup/teardown
- Organização por endpoint (arquivos separados)
- Reutilização de código através de helpers
- Documentação inline para cenários complexos

### 5.3 Cobertura de Testes

**Meta de Cobertura:**
- ✅ Cenários positivos (happy path): 100%
- ✅ Cenários negativos principais: 100%
- ✅ Validações de campos obrigatórios: 100%
- ⚠️ Cenários de borda: 70%

**Cobertura Atual:**
- Usuários: 11/11 cenários (100%)
- Login: 0/6 cenários (0%)
- Produtos: 0/10 cenários (0%)
- **Total: 11/27 cenários (40.7%)**

**Cobertura Projetada após implementação:** 27/27 cenários (100%)

## 6. Critérios de Entrada e Saída

### 6.1 Critérios de Entrada

Para iniciar a execução dos testes, os seguintes critérios devem ser atendidos:

- ✅ API ServeRest disponível e acessível
- ✅ Ambiente de testes configurado (Python, Pytest, Requests instalados)
- ✅ Dependências instaladas (`requirements.txt`)
- ✅ Conectividade de rede estável
- ✅ Dados de teste preparados (não aplicável - geração dinâmica)

### 6.2 Critérios de Saída

A execução dos testes pode ser finalizada quando:

- ✅ Todos os testes planejados foram executados
- ✅ Todos os testes implementados executando com sucesso.
- ✅ Nenhum bug bloqueador ou crítico foi identificado
- ✅ Evidências documentadas (logs, screenshots se aplicável)

### 6.3 Critérios de Suspensão

Os testes devem ser suspensos se:

- ❌ API ServeRest indisponível por mais de 30 minutos
- ❌ Taxa de falha > 30% (indica problema ambiental)
- ❌ Bugs bloqueadores identificados que impedem testes subsequentes
- ❌ Mudanças não documentadas na API

## 7. Riscos e Mitigação

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| API indisponível durante execução | Média | Alto | Implementar retry automático, testes de health check |
| Mudanças não documentadas na API | Média | Alto | Manter contrato de API versionado, alertas em CI/CD |
| Dados de teste conflitantes | Baixa | Médio | Uso de UUID e cleanup após testes |
| Dependência entre testes | Baixa | Alto | Design de testes independentes, fixtures isoladas |
| Timeout em requisições | Média | Médio | Configurar timeouts adequados, monitorar latência |
| Token expirado durante execução | Baixa | Médio | Renovação automática de token, validação antes de uso |

## 8. Premissas e Dependências

### 8.1 Premissas

- A API ServeRest está em um ambiente estável e acessível
- A documentação da API está atualizada
- O comportamento esperado da API está claramente definido
- Ambiente de testes não impacta dados de produção
- API permite múltiplas requisições simultâneas

### 8.2 Dependências

**Técnicas:**
- Python 3.14.5
- Pytest
- Requests
- UUID (biblioteca padrão Python)
- Git/GitHub para versionamento

**Ambientais:**
- API ServeRest disponível (URL base configurável)
- Conexão de internet estável
- Permissões para criar/excluir dados via API

**Conhecimento:**
- Documentação da API ServeRest
- Especificação de requisitos funcionais
- Regras de negócio para Usuários, Login e Produtos

## 9. Métricas e Indicadores

### 9.1 Métricas de Execução

- **Total de Testes**: 27 cenários planejados
- **Taxa de Sucesso**: (Testes Passou / Total de Testes) × 100
- **Taxa de Falha**: (Testes Falhou / Total de Testes) × 100
- **Tempo de Execução**: Tempo total da suíte
- **Tempo Médio por Teste**: Tempo total / Número de testes

### 9.2 Métricas de Qualidade

- **Cobertura de Endpoints**: 3/3 endpoints principais (100%)
- **Cobertura de Cenários Positivos**: Meta 100%
- **Cobertura de Cenários Negativos**: Meta 100%
- **Bugs Encontrados**: Número de defeitos identificados
- **Severidade dos Bugs**: Crítico, Alto, Médio, Baixo

## 11. Entregas

- ✅ Suite de testes automatizados (código-fonte Python)
- ✅ Arquivo `requirements.txt` com dependências
- ✅ Documentação de execução (README)
- 🔄 Relatórios de execução (Opcional)
- 🔄 Integração com GitHub Actions (Opcional)
- ✅ Plano de Testes (este documento)


---

**Legenda:**
- ✅ Concluído
- 🔄 Em andamento / Planejado
- ❌ Bloqueado
- ⚠️ Atenção necessária

**Versão do Documento:** 1.0  
**Data de Criação:** [15/06/2026]  
**Última Atualização:** [15/06/2026]  
**Autor:** Rayane Duarte
