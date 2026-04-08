from google import genai
from google.genai import types
import os
from services.functions_services import get_status_order, update_status_order, generate_complaint,generate_discount_coupon
from services.business_rules import business_rules

# INTEGRANDO COM GEMINI
# Criando cliente para interagir com Gemini
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

# REGRAS DE NEGOCIO

# 3. Configuração de Geração com Tools e System Instruction [2, 9]
config = types.GenerateContentConfig(
    system_instruction=business_rules,
    tools=[ get_status_order, update_status_order,generate_complaint,generate_discount_coupon],
    temperature=1.0  # Valor recomendado para o Gemini 3 [10]
)
# Criando chat do Gemini para acompanhar historico de conversas
chat = client.chats.create(model="gemini-3-flash-preview", config=config)

# enviando perguntas a api do Gemini - teste inicial
# está aqui por enquanto só pra ver se Gemini esta funcionando
#response = chat.send_message("Em que ano Ada Love Lace nasceu?")
#print(response.text)