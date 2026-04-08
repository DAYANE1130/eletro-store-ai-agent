from services.gemini_integration_services import client
import time

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