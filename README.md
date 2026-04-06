# ELETRO STORE AI AGENT

# 🛍️ Assistente Virtual de Atendimento Inteligente (MVP)

[cite_start]Este projeto consiste em um **MVP (Minimum Viable Product)** de um assistente de atendimento para uma loja de eletrônicos, focado em automatizar interações complexas e processos de tomada de decisão através de IA Generativa[cite: 10, 11].

## 📄 Contexto do Problema
[cite_start]Lojas de e-commerce enfrentam gargalos no atendimento manual de tarefas repetitivas[cite: 25]. Este assistente resolve:
* [cite_start]**Dúvidas Frequentes:** Respostas sobre produtos e políticas da loja[cite: 25].
* [cite_start]**Processamento de Arquivos:** Leitura de comprovantes e imagens de defeitos via Visão Computacional[cite: 25].
* [cite_start]**Ações Transacionais:** Integração com funções internas para resolver problemas em tempo real[cite: 23].
* [cite_start]**Tomada de Decisão (If Mágico):** Uso de IA para aplicar regras de negócio e decidir ações automaticamente[cite: 11].

## 🛠️ Tecnologias e Ferramentas
* [cite_start]**Linguagem:** Python[cite: 13, 37].
* [cite_start]**IA Generativa:** Google Gemini API (LLM & Vision)[cite: 14, 25].
* [cite_start]**Framework Web:** Flask[cite: 13].
* [cite_start]**Interface:** Gradio[cite: 22].
* [cite_start]**Arquitetura:** Function Calling e Lógica de Negócio Baseada em Agentes[cite: 10].
* **Deploy:** Hugging Face Spaces.

## ✅ Funcionalidades Implementadas
* [cite_start]**Chatbot Multimodal:** Suporte para mensagens de texto, imagens e PDFs[cite: 24, 25].
* **Function Calling (Ações Internas):**
    * `atualizar_status_pedido`: Altera o estado da entrega no sistema.
    * `gerar_cupom_desconto`: Cria cupons personalizados com base na interação.
    * `registrar_reclamacao`: Formaliza feedbacks de produtos com defeito.
* [cite_start]**Motor de Regras (If Mágico):** A IA analisa o histórico e os dados do cliente para decidir, de forma autônoma, qual função disparar seguindo as diretrizes da loja[cite: 11].

## 🏗️ Arquitetura do Projeto
[cite_start]O projeto segue uma estrutura organizada para facilitar a manutenção e escalabilidade[cite: 26]:
```text
├── app.py              # Ponto de entrada (Flask + Gradio)
├── core/               # Lógica de negócio e "If Mágico"
├── agents/             # Integração com Gemini e definições de Functions
├── utils/              # Processamento de arquivos (PDF/Imagens)
├── requirements.txt    # Dependências do projeto
└── .env                # Variáveis de ambiente (API Keys)
```

## 🚀 Como Executar
1. [cite_start]Clone o repositório: `git clone https://github.com/DAYANE1130/nome-do-repo`[cite: 6].
2. Instale as dependências: `pip install -r requirements.txt`.
3. Configure sua `GOOGLE_API_KEY` no arquivo `.env`.
4. Execute a aplicação: `python app.py`.

---
[cite_start]**Desenvolvido por Dayane Martins** *Focado em Backend, IA e Automação de Processos.* [cite: 1, 4]

---

### 💡 Dica de Sucesso (Recrutadora):
[cite_start]Ao publicar no LinkedIn, destaque que o **"If Mágico"** não é um código estático, mas sim a **IA interpretando regras de negócio complexas** para agir sozinha[cite: 11]. Isso demonstra que você entende o conceito de **Agentes Autônomos**, a tendência mais forte de 2026.
