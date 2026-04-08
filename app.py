from flask import Flask, render_template, request
from services.gemini_integration_services import chat
from utils.gemini_upload import upload_file
from google.api_core.exceptions import InvalidArgument
import time
import gradio as gr

app = Flask(__name__)

# criando função de bate papo para  enviar ao Gradio


def get_response(message, _history):
    time.sleep(5)  # Espera 5 segundos antes de CADA chamada
    try:
        text = message['text']
        prompt = [text]
        file = upload_file(message)  # file é uma lista
        prompt.extend(file)
        response = chat.send_message(prompt)
        print("SOU A RESPOSTA da função de bate papo", response.text)
    except InvalidArgument as e:
        print(f"Erro: {e}")
        response = chat.send_message(
            f"O usuário te enviou um arquivo para você ler e obteve o erro: {e}.Pode explicar o que houve e dizer quais tipos de arquivos você dá suporte? Assuma que a pessoa não sabe programação e não quer ver o erro original. Explique de forma simples e concisa."
        )
    return response.text


# INTEGRANDO COM O GRADIO -testando primeiro contato
gr.ChatInterface(
    fn=get_response,  
    title="Assistente Virtual Eletro Store",
    multimodal=True
    ).launch()

# Rotas básicas


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
