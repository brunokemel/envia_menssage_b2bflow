# API WhatsApp com FastAPI + Supabase Pooler + Z-API

## Objetivo

Buscar um cliente no banco PostgreSQL do Supabase utilizando o Connection Pooler e enviar uma mensagem via WhatsApp usando a Z-API.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

---

## Estrutura do Projeto

```text
projeto/
│
├── .env
├── main.py
├── routers.py
├── requirements.txt
└── README.md
```

---

## Tecnologias

* FastAPI
* PostgreSQL (Supabase Pooler)
* Psycopg
* Z-API
* Python Dotenv

---

## Instalação

Clone o projeto:

```bash
git clone <repositorio>
cd projeto
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Dependências

Arquivo `requirements.txt`:

```txt
fastapi
uvicorn
python-dotenv
requests
psycopg[binary]
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
# Banco de Dados (Supabase Pooler)
DATABASE_URL=postgresql://usuario:senha@host:6543/postgres

# Z-API
ZAPI_INSTANCE_ID=seu_id_da_instancia
ZAPI_TOKEN=seu_token_da_instancia
```

### Onde encontrar os dados da Z-API

No painel da Z-API:

1. Acesse sua instância.
2. Copie o **ID da Instância**.
3. Copie o **Token da Instância**.

---

## Banco de Dados

Criar a tabela:

```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);
```

Inserir alguns registros para teste:

```sql
INSERT INTO clientes (nome, telefone)
VALUES
('Bruno', '5591999999999'),
('João', '5591888888888');
```
(Recomendo usar pelo postman as requisicoes pela flexbilidade, está logo a baixo )
---

## Executando a API

Inicie o servidor:

```bash
python -m uvicorn main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

---

## Documentação Swagger

Acesse:

```text
http://127.0.0.1:8000/docs
```

---

# Testando com Postman

## 1. Criar Cliente

### Método

```http
POST
```

### URL

```text
http://127.0.0.1:8000/clientes
```

### Headers

```http
Content-Type: application/json
```

### Body (raw → JSON)

```json
{
  "nome": "Teste",
  "telefone": "55919855099999" - adicione o número valido de destino
}
```

### Resposta Esperada

```json
{
  "success": true,
  "id": 1,
  "nome": "Teste",
  "telefone": "55919855099999" - adicione o número valido de destino
}
```

---

## 2. Enviar Mensagem

### Método

```http
POST
```

### URL

```text
http://127.0.0.1:8000/enviar/1
```

Onde:

```text
1 = ID do cliente cadastrado
```

### Body

Nenhum.

### Resposta

```json
{
  "success": true,
  "cliente": "Teste",
  "telefone": "55919855099999" - adicione o número valido de destino
}
```

---

## Fluxo Completo

1. Criar um cliente usando `POST /clientes`.
2. O cliente é salvo no PostgreSQL do Supabase.
3. Obter o ID retornado.
4. Executar `POST /enviar/{id}`.
5. A API busca o cliente no banco.
6. Monta a mensagem:

```text
Olá, Teste! tudo bem com você?
```

7. Envia a mensagem pela Z-API.
8. Retorna o resultado da operação.

---

## Exemplo Completo

### Cadastro

```http
POST http://127.0.0.1:8000/clientes
```

```json
{
  "nome": "Teste",
  "telefone": "55919855099999" - adicione o número valido de destino
}
```

### Envio

```http
POST http://127.0.0.1:8000/enviar/1
```

---

## Endpoints

### Criar Cliente

```http
POST /clientes
```

### Enviar Mensagem

```http
POST /enviar/{cliente_id}
```

---

## Possíveis Erros

### Cliente não encontrado

```json
{
  "detail": "Cliente não encontrado"
}
```

### Erro de conexão com o banco

Verifique:

```env
DATABASE_URL
```

### Erro da Z-API

Verifique:

```env
ZAPI_INSTANCE_ID
ZAPI_TOKEN
```

e confirme na documentação da sua instância qual é o endpoint correto para envio de mensagens.

---

## Estrutura da Consulta SQL

```sql
SELECT nome, telefone
FROM clientes
WHERE id = $1;
```
