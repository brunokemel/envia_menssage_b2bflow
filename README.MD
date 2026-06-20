# API WhatsApp com FastAPI + Supabase + Z-API

## Objetivo

Buscar um cliente no Supabase e enviar uma mensagem via WhatsApp usando a Z-API.

Mensagem enviada:

Olá, <nome_contato> tudo bem com você?

---

## Estrutura

```text
projeto/
│
├── .env
├── main.py
├── routers.py
├── requirements.txt
└── README.md
```

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

Criar um arquivo `.env`:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

## Executar

```bash
uvicorn main:app --reload
```

## Documentação

```text
http://localhost:8000/docs
```

## Endpoint

### Enviar mensagem

```http
POST /enviar/{cliente_id}
```

Exemplo:

```http
POST /enviar/1
```

## Banco de dados

Tabela:

```sql
create table clientes (
    id serial primary key,
    nome text not null,
    telefone text not null
);
```