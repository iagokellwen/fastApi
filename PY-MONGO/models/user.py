from pydantic import BaseModel


class Chat(BaseModel):
    pergunta: str
