import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from PyPDF2 import PdfReader


genai.configure(api_key="AIzaSyAVxFBRdA3YZ5wmmb40txBj_DdCHpGV0Sk")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192
}

safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

model = genai.GenerativeModel(model_name='gemini-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings)


def extract_pdf(caminho: str) -> list[str]:
    # Se o caminho estiver vazio, retorne uma lista vazia
    if not caminho:
        return ["--- No PDF file provided ---"]

    parts = [f"--- START OF PDF {caminho} ---"]
    try:
        with open(caminho, "rb") as file:
            reader = PdfReader(file)
            for page_number in range(len(reader.pages)):
                page = reader.pages[page_number]
                parts.append(f"--- PAGE {page_number} ---")
                parts.append(page.extract_text())
    except Exception as e:
        parts.append(f"--- Error reading PDF: {str(e)} ---")

    return parts


def chat_bot(pergunta):
    chat = model.start_chat(history=[
        {
            "role": "user",
            "parts": extract_pdf("uploads/contrato.pdf")

        },
    ])
    response = chat.send_message(pergunta)
    return response


'''bem_vindo = "Bem vindo ao assistente leitor de PDF IA"
print(len(bem_vindo) * "-")
print(bem_vindo)
print(len(bem_vindo) * "-")
print("Digite sair para encerrar!")
print()

while True:
    pergunta = input("Mensagem: ")
    if pergunta.lower() == "sair":
        break

    response = chat.send_message(pergunta)
    print("IA:", response.text, "\n")
    print("-"*70)

print("Chat Encerrado")'''


'''chat.send_message("Qual o lucro liquido da empresa?")
print(chat.last.text)'''
