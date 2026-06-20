import os 
import psycopg
import requests

from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel

#carrega variaveis de ambient do .env(.exemolo.env use de base para criar o seu .env)
load_dotenv()

router = APIRouter()

DATABASE_URL = os.getenv("DATABASE_URL")

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

#rotas
#modelo de dados para cliente
class Cliente(BaseModel):
    nome: str
    telefone: str

@router.post("/clientes")
async def criar_cliente(cliente: Cliente):

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO clientes (nome, telefone)
                VALUES (%s, %s)
                RETURNING id
                """,
                (cliente.nome, cliente.telefone)
            )

            cliente_id = cur.fetchone()[0]

            conn.commit()

    return {
        "success": True,
        "id": cliente_id,
        "nome": cliente.nome,
        "telefone": cliente.telefone
    }

#rota para enviar menssagem
@router.post("/enviar/{cliente_id}")
def enviar_menssagem(cliente_id: int):
    try:
        with psycopg.connect(DATABASE_URL) as conn:
            with conn.cursor() as cur:

                cur.execute(
                    """
                    SELECT nome, telefone FROM clientes WHERE id = %s
                    """,
                    (cliente_id,)
                )

                cliente = cur.fetchone()

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado"
            )
        
        nome, telefone = cliente

        menssagem = f"Ola, {nome}! tudo bem com você?"

        url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

        payload = {
            "phone": telefone,
            "message": menssagem
        }


        respostas = requests.post(
            url,
            json=payload,
            timeout=10
        )



        return {
            "sucess": True,
            "cliente": nome,
            "telefone": telefone,
            "status_code": respostas.status_code,
            "zapi_response": respostas.json()
        }
    
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )