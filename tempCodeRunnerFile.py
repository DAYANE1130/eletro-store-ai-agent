from database.database import get_customer


def get_status_order(id_user: str, num_order: int) -> str:
    print(
        f"DEBUG: IA chamou a função GET STATUS ORDER com ID {id_user,num_order}")
    """
    PERGUNTA sobre status do pedido
    Busca o status de um pedido com base no ID do cliente e número do pedido.
    """
    user = get_customer(id_user)
    if (user):
        if user["id_cliente"] == id_user and user["num_pedido"] == num_order:
            return f"Olá {user['nome']}, o status do seu pedido #{user['num_pedido']} é: {user['status_pedido']}."

    # 3. Caso o loop termine sem encontrar uma combinação válida
    return "Desculpe, não encontrei um pedido com esses dados. Verifique o ID e o número do pedido."

# --- Exemplos de Uso ---


# Teste com cliente existente
print(get_status_order("2", 1002))
# Saída: Olá Bruno Lima, o status do seu pedido #1002 é: Processando.

# Teste com dados incorretos
print(get_status_order("1", 9999))
# Saída: Desculpe, não encontrei um pedido com esses dados...
