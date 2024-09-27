# Guia para Colocar o Chat no Ar - Desafio LizardTI (FastAPI)
Passo 1: Clonar o Repositório
Clone o repositório do GitHub com o seguinte comando:

bash
Copiar código
git clone https://github.com/iagokellwen/fastApi.git
Passo 2: Instalar Dependências
Instale as bibliotecas necessárias listadas no arquivo requirements.txt.

Opcional: Crie um ambiente virtual para isolar as dependências do projeto. Para isso, use o comando:

Windows:
bash
Copiar código
python -m venv <nome_do_ambiente>
Linux:
bash
Copiar código
python3 -m venv <nome_do_ambiente>
Após criar o ambiente, ative-o:

Windows:
bash
Copiar código
<nome_do_ambiente>\Scripts\activate
Linux:
bash
Copiar código
source <nome_do_ambiente>/bin/activate
Para instalar as dependências, execute o seguinte comando:

Windows:
bash
Copiar código
pip install -r requirements.txt --user
Linux:
bash
Copiar código
sudo pip install -r requirements.txt
Passo 3: Configurar o Banco de Dados
Se você tiver o MongoDB instalado localmente, a aplicação já estará configurada para conectar-se ao localhost.

Caso esteja utilizando um cluster MongoDB na nuvem, basta alterar o usuário e a senha no arquivo db.py, localizado na pasta config.

Passo 4: Executar a Aplicação
Com tudo configurado, estando no diretório do projeto, execute o seguinte comando no terminal para rodar a aplicação com o FastAPI:

bash
Copiar código
uvicorn main:app --reload
Esse comando iniciará o servidor com reload automático sempre que houver alterações no código.

Agora, seu chat deve estar disponível!
