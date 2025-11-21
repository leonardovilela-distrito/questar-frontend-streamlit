from typing import TypedDict
from dataclasses import dataclass
import requests
import os

class SqlRow(TypedDict):
    manufacturer: str
    num_vehicles: int

@dataclass
class AskBedrock:
    conversation_id: str
    response: str
    sql_query: str | None
    sql_data: list[SqlRow]

def ask_bedrock(question: str, chat_id) -> AskBedrock:
    headers = { "x-api-token": os.getenv("API_TOKEN") }
    base_url = os.getenv("API_BASE_URL")
    payload = {
        "question": question,
        "conversation_id": chat_id
    }
    response = requests.post(f"{base_url}/ask", json=payload, headers=headers)

    if response.status_code != 200:
        return AskBedrock(
            conversation_id=chat_id,
            response="Erro",
            sql_query=None,
            sql_data=[]
        )
    data = response.json()

    if "message" in data:
        return AskBedrock(
            conversation_id=chat_id,
            response=data["message"],
            sql_query=None,
            sql_data=[]
        )

    return AskBedrock(**data)
