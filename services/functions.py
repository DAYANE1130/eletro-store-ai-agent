from database.database import get_customer
import random


def get_status_order(id_user: str, num_order: int) -> str:
    print(
        f"DEBUG: IA chamou a função GET STATUS ORDER com ID {id_user,num_order}")
    """
    PERGUNTA sobre status do pedido
    Busca o status de um pedido com base no ID do cliente e número do pedido.
    """
    user = get_customer(id_user)
    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):
        if user["num_pedido"] == num_order:
            return f"Olá {user['nome']}, o status do seu pedido #{user['num_pedido']} é: {user['status_pedido']}."
        return "Desculpe, não encontrei um pedido com esses dados. Verifique por favor o número do pedido."

# --- Exemplos de Uso ---


# Teste com cliente existente
# print(get_status_order("2", 1002))
# Saída: Olá Bruno Lima, o status do seu pedido #1002 é: Processando.

# Teste com dados incorretos
# print(get_status_order("1", 9999))
# Saída: Desculpe, não encontrei um pedido com esses dados...
# print(get_status_order("1", 9999))


def update_status_order(id_user: str, num_order: int, new_status: str) -> str:
    print(
        f"DEBUG: IA chamou a função UPDATE STATUS ORDER com dados {id_user, num_order,new_status}")

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
            print(user)
            return f"Sucesso! {user['nome']},o status do seu pedido{num_order} foi alterado de '{status_anterior}' para '{new_status}'."

    # 4. Caso o ID não seja encontrado
    return f"Erro: Não foi possível atualizar seu pedido para {new_status}"


# --- Exemplos de Uso ---
# Atualizando o status do Davi Rocha (ID 4)
# print(update_status_order("4",1004))
# print(update_status_order("4", 1004, "Aguardando Pagamento"))
user = get_customer("5")
# print(user)
# Verificando se mudou mesmo no dicionário original
# print(f"Novo status no sistema: {user['status_pedido']}")


def generate_complaint(id_user: str, order_number: int) -> str:
    """
    Registra uma reclamação formal na base de dados e gera um protocolo.
    -Se o cliente enviar uma imagem de um produto com defeito,deve registrar a reclamação.
    -Chamar a função `generate_complaint` e fornecer um número de protocolo ao cliente.
    """
    print(
        f"DEBUG: IA chamou a função GENERATE COMPLAIM com ID {id_user, order_number}")

    user = get_customer(id_user)

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):

        if (user["protocol_number"] == False):
            user["foto_produto_defeito_enviada"] = True
            user["status_insatisfacao"] = True
            # 3. Geramos um numero de protocolo
            protocol_number = f"PROT-{user['id_cliente']}-{random.randint(10000, 99999)}"
            user["protocol_number"] = protocol_number
            protocol_number = user["protocol_number"]
            print("sou o user da generate complaint", user)
            return f"Sucesso!{user['nome']}, Sua solicitação foi registrada sobre o pedido {order_number} e o numero do protocolo é '{protocol_number}'"

        return f"Erro:{user['nome']}, não foi possível registrar sua reclamação"

# --- Exemplos de Uso ---
# Gerando reclamação status de Ana Silva  (ID 1)
# print(generate_complaint("1", 1001))

# Testando com um  usuário que não existe
# print(generate_complaint("11",1111))

# Testando de passa o mesmo numero para Ana Silva
# print(generate_complaint("1", 1001))


def generate_discount_coupon(id_user: str) -> str:
    """
    Registra uma reclamação formal na base de dados e gera um protocolo.
     # Se o cliente for recorrente ou estiver insatisfeito("cliente_recorrente" == True ou "status_insatisfacao" == True), pode oferecer um cupom de desconto.
    # Chamar a função `generate_discount_coupon` e enviar o código ao cliente.
    """
    print(
        f"DEBUG: IA chamou a função generate_discount_coupon com ID {id_user}")
    user = get_customer(id_user)

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):

        if user["cupom_desconto_ativo"] is False:
            # Geramos o cupom
            novo_cupom = f"DESC-{user['id_cliente']}-{random.randint(1000, 9999)}"
            user["cupom_desconto_ativo"] = novo_cupom

            # Recuperamos o valor (seja o que acabamos de criar ou o que já existia)
            cupom_final = user["cupom_desconto_ativo"]

            return f"Boas notícias, {user['nome']}! Você tem um cupom disponível: {cupom_final}."

        return f"Olá {user['nome']}, no momento não há cupons disponíveis para este perfil."


# Gerando cupom para Ana Silva  (ID 1)
# print(generate_discount_coupon("1"))

# Testando cliente não recorrente e não insatisfeito
# print(generate_discount_coupon("4"))

# Testando com um  usuário que não existe
# print(generate_discount_coupon("11"))
