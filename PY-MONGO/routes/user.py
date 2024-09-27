from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from models.user import Chat
from config.db import conn
from schemas.user import chatEntity, chatsEntity
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import app
from config.db import conn


chat = APIRouter()


@chat.post('/postar')
async def create_chat(chat: Chat):
    # Extrai a pergunta do objeto recebido
    pergunta = chat.pergunta

    # Gera a resposta usando a função do chatbot
    response = app.chat_bot(pergunta)

    # Acesse diretamente o texto gerado na resposta
    resposta = response.candidates[0].content.parts[0].text

    # Cria um dicionário que inclui pergunta e resposta como strings
    chat_dict = {
        "pergunta": pergunta,
        "resposta": resposta
    }
    # Insere no banco de dados apenas o dicionário com strings simples
    conn.mydb.chat.insert_one(chat_dict)

    return {
        "pergunta": pergunta,
        "resposta": resposta
    }


@chat.get('/buscar')
async def find_all_chats():
    print(chatsEntity(conn.mydb.chat.find()))
    return chatsEntity(conn.mydb.chat.find())


templates = Jinja2Templates(directory="templates")


@chat.get('/', response_class=HTMLResponse)
async def index(request: Request):
    chats = (chatsEntity(conn.mydb.chat.find()))
    context = {'request': request, 'chats': chats}
    return templates.TemplateResponse("index.html", context)

UPLOAD_DIR = "uploads"
# Verifica se a pasta de upload existe, senão cria
os.makedirs(UPLOAD_DIR, exist_ok=True)


@chat.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Verifica se o arquivo é um PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, detail="O arquivo deve ser um PDF")

    # Armazena o nome do arquivo em uma variável
    uploaded_file_name = file.filename

    # Caminho completo do arquivo
    file_location = os.path.join(UPLOAD_DIR, "contrato.pdf")

    try:
        # Salva o arquivo no diretório especificado
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"info": f"Arquivo {file.filename} salvo com sucesso em {file_location}"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao salvar o arquivo: {str(e)}")

if __name__ == "__main__":
    import uvicorn
