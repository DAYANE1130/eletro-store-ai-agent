# ELETRO STORE AI AGENT


```markdown
# 🛍️ Assistente Virtual de Atendimento ao Cliente (MVP)

Este repositório contém um **Mínimo Produto Viável (MVP)** de um assistente inteligente projetado para uma loja online de eletrônicos. O objetivo é automatizar o suporte ao cliente, integrando processamento de linguagem natural, visão computacional e tomada de decisão autônoma.

## 📄 Contexto do Problema
Lojas de e-commerce enfrentam alta demanda em tarefas repetitivas que atrasam o suporte. Este projeto resolve:
* **Dúvidas Frequentes:** Responde sobre produtos, pedidos e políticas da loja.
* **Processamento Multimodal:** Analisa comprovantes de pagamento (PDF) e imagens de produtos com defeito enviadas pelos clientes.
* **Ações Transacionais:** Integração com funções internas para resolver problemas em tempo real sem intervenção humana.
* **Tomada de Decisão (If Mágico):** Utiliza IA para analisar dados do cliente e decidir automaticamente qual ação tomar com base em regras de negócio pré-definidas.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python
* **IA Generativa:** Google Gemini API (LLM & Vision)
* **Framework Web:** Flask
* **Interface do Usuário:** Gradio
* **Arquitetura:** Function Calling e Lógica de Negócio Assistida por IA
* **Hospedagem:** Deploy realizado no Hugging Face Spaces

## ✅ Funcionalidades Principais
* **Chatbot Interativo:** Interface que permite o envio de mensagens de texto, imagens e documentos.
* **Chamada de Funções (Function Calling):** A IA decide autonomamente quando acionar ferramentas internas para:
    * Atualizar o status de um pedido.
    * Gerar cupons de desconto personalizados.
    * Registrar reclamações técnicas sobre produtos.
* **Inteligência de Negócio (If Mágico):** Implementação de lógica generativa que orienta o comportamento da IA de acordo com as diretrizes da empresa.

## 🏗️ Estrutura do Projeto
```text
├── app.py              # Ponto de entrada (Flask + Gradio)
├── core/               # Lógica de negócio e regras do "If Mágico"
├── agents/             # Configuração do Gemini e definições de funções
├── utils/              # Processamento de arquivos (Imagens e PDFs)
├── requirements.txt    # Dependências do sistema
└── .env                # Variáveis de ambiente (API Keys)
```

## 🚀 Como Executar
1. Clone este repositório: `git clone https://github.com/DAYANE1130/seu-repositorio`
2. Instale as dependências: `pip install -r requirements.txt`
3. Crie um arquivo `.env` e adicione sua `GOOGLE_API_KEY`.
4. Inicie a aplicação: `python app.py`

---
**Desenvolvido por Dayane Martins** *Foco em Backend, IA Generativa e Soluções Cloud.*
```

