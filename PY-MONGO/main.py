from fastapi import FastAPI
from routes.user import chat
from fastapi import FastAPI, Request


app = FastAPI()
app.include_router(chat)
