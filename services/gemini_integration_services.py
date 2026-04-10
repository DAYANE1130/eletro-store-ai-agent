from google import genai
from google.genai import types
import os
from services.functions_services import get_status_order, update_status_order, generate_complaint,generate_discount_coupon
from services.business_rules_services import business_rules

# INTEGRANDO COM GEMINI
client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])


# Configuração de Geração com Tools e System Instruction
config = types.GenerateContentConfig(
    system_instruction=business_rules,
    tools=[ get_status_order, update_status_order,generate_complaint,generate_discount_coupon],
    temperature=1.0
)
# Criando chat do Gemini para acompanhar historico de conversas
chat = client.chats.create(model="gemini-3-flash-preview", config=config)

