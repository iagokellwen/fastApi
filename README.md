# fastApi - Engenharia de Prompt
# Desafio LizardTI

#Guia para colocar o chat no ar

#passo 1:
clonar o repositorio do git: https://github.com/iagokellwen/fastApi.git
#passo 2:
instalar o arquivo requeriments.txt disponibilizado para que posso baixar as bibliotecas necessarias para a aplicação.
opcional criar um ambiente virtual, caso queira criar, use o comando: python -m venv <nome_do_ambiente> ou python3 para linux
execute o comando:  
windows: pip install -r requirements.txt --user
linux: sudo pip install -r requirements.txt
#passo 3:
caso tenha um banco de dados mongo db instalado a aplicação já vem pre-definida para localhost, mas caso tenha um cluster na nuvem
já existe um codigo pré-configurado, só alterar o usuario e senha no arquivo db.py na pasta config
#passo 4:
se já estiver na pasta do py-mongo, execute o comando no terminal:

#uvicorn main:app --reload

