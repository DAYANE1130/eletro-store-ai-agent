from flask import Flask, render_template, request
from services.config_gemini import client,chat
import time
import gradio as gr

app = Flask(__name__)

# criando função que permite upload dos arquivos enviados pelo usuário


def upload_file(message):

    uploaded_files = []  # todos os arquivos
    if message['files']:  # verifico se existe algum arquivo para upload
        for path_file in message["files"]:  # passear no mundo do array
            uploaded_file = client.files.upload(file=path_file)  # upload de
            while uploaded_file.state.name == "PROCESSING":

                time.sleep(5)  # vai esperar quanto o status está
                uploaded_file = client.files.get(name=uploaded_file.name)

            uploaded_files.append(uploaded_file)

    return uploaded_files

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
        return response.text
    except Exception as e:
        print(f"Erro: {e}")


# INTEGRANDO COM O GRADIO -testando primeiro contato
gr.ChatInterface(fn=get_response, multimodal=True).launch()

# Rotas básicas


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
