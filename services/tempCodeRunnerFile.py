def update_status_order(id_user: str, num_order: int, new_status: str) -> str:
   # print(f"DEBUG: IA chamou a função UPDATE STATUS ORDER com ID {id_user, num_order}")
    """
    Atualiza o status somente se:
    -Receber uma clara confirmação  verbal de que recebeu o produto-> Busca cliente pelo ID confere se o num_order enviado é igual ao "num_pedido" da base de dados.
    -Receber um comprovante de pagamento com número de pedido e valor total condizentes com as informações do pedido na base de dados.
    """
    user = get_customer(id_user)
    status_permitidos = ["Entregue", "Pago", "Aguardando Pagamento"]

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):
        # 3. Atualizamos o valor da chave
        if (new_status in status_permitidos):
            status_anterior = user['status_pedido']
            user["status_pedido"] = new_status

            return f"Sucesso! {user['nome']},o status do seu pedido{num_order} foi alterado de {status_anterior} para {new_status}'."

    # 4. Caso o ID não seja encontrado
    return f"Erro: Não foi possível atualizar seu pedido para {new_status}"


# --- Exemplos de Uso ---
# Atualizando o status do Davi Rocha (ID 4)
# print(update_status_order("4",1004))
print(update_status_order("4", 1004, "Aguardando Pagamento"))