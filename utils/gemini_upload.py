from services.gemini_integration_services import client
import time

# criando função que permite upload dos arquivos enviados pelo usuário
def upload_file(message):

    uploaded_files = []
    if message['files']:
        for path_file in message["files"]:  
            uploaded_file = client.files.upload(file=path_file) 
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(5)  
                uploaded_file = client.files.get(name=uploaded_file.name)

            uploaded_files.append(uploaded_file)

    return uploaded_files