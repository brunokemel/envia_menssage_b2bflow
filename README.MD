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
DATABASE_URL=postgresql://postgres.xxxxx:SENHA@aws-0-sa-east-1.pooler.supabase.com:6543/postgres

# Z-API
ZAPI_INSTANCE_ID=sua_instancia
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

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

---

## Executando a API

Inicie o servidor:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```text
http://localhost:8000
```

---

## Documentação Swagger

Acesse:

```text
http://localhost:8000/docs
```

---

## Endpoint

### Enviar mensagem para um cliente

```http
POST /enviar/{cliente_id}
```

Exemplo:

```http
POST /enviar/1
```

---

## Fluxo da API

1. Recebe o ID do cliente.
2. Consulta o PostgreSQL no Supabase.
3. Busca nome e telefone.
4. Monta a mensagem:

```text
Olá, Bruno tudo bem com você?
```

5. Envia a mensagem pela Z-API.
6. Retorna o resultado da operação.

---

## Exemplo de Resposta

```json
{
  "success": true,
  "cliente": "Bruno",
  "telefone": "5591999999999",
  "mensagem": "Olá, Bruno tudo bem com você?"
}
```

---

## Estrutura da Consulta SQL

```sql
SELECT nome, telefone
FROM clientes
WHERE id = $1;
```

---

## Melhorias Futuras

* Envio em massa para todos os clientes
* Agendamento de mensagens
* Templates personalizados
* Logs de envio
* Histórico de mensagens
* Integração com filas (RabbitMQ ou Redis)
* Autenticação JWT
* Rate Limit para proteção da API

```
```
