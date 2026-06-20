import os 
import requests

from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from supabase import create_client

#carrega variaveis de ambient do .env(.exemolo.env use de base para criar o seu .env)
load_dotenv()

router = APIRouter()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

#routas
@router.post("/enviar/{cliente_id}")
def enviar_menssagem(cliente_id: int):
    try:

        resultado = (
            supabase
            .table("clientes")
            .select("nome,telefone")
            .eq("id", cliente_id)
        )

        cliente = resultado.data

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado"
            )
        
        nome = cliente["nome"]
        telefone = cliente["telefone"]

        menssagem = f"Ola, {nome}! tudo bem com você?"

        url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-messages"

        payload = {
            "phone": telefone,
            "message": menssagem
        }

        headers = {
            "Client-Token": ZAPI_CLIENT_TOKEN,
            "Content-Type": "application/json"
        }

        respostas = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return {
            "sucesso": True,
            "cliente": nome,
            "telefone": telefone,
            "zapi": respostas.json()
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )