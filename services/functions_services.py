from database.database import get_customer
from typing import Optional
import random


def get_status_order(id_user: Optional[str] = None, num_order: Optional [int] = None) -> str:
    """
    Recupera o status do pedido.
    Args:
        id_user: O ID único do cliente (opcional).
        num_order: O número do pedido (opcional, aceita apenas números inteiros).
    """
    user = get_customer(id_user, num_order)
    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):
        if user["num_pedido"] == num_order:
            return f"Olá {user['nome']}, o status do seu pedido #{user['num_pedido']} é: {user['status_pedido']}."
        return "Desculpe, não encontrei um pedido com esses dados. Verifique por favor o número do pedido."



def update_status_order(num_order: int, new_status: str) -> str:
    """
    Atualiza o status somente se:
    -Receber uma clara confirmação  verbal de que recebeu o produto-> Busca cliente pelo ID confere se o num_order enviado é igual ao "num_pedido" da base de dados.
    -Receber um comprovante de pagamento com número de pedido e valor total condizentes com as informações do pedido na base de dados.
    """
    user = get_customer(num_order)
    status_permitidos = ["Entregue", "Pago", "Aguardando Pagamento"]

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):
        if (new_status in status_permitidos):
            status_anterior = user['status_pedido']
            user["status_pedido"] = new_status
            return f"Sucesso! {user['nome']},o status do seu pedido{num_order} foi alterado de '{status_anterior}' para '{new_status}'."

    return f"Erro: Não foi possível atualizar seu pedido para {new_status}"


def generate_complaint(id_user: str, order_number: int) -> str:
    """
    Registra uma reclamação formal na base de dados e gera um protocolo.
    -Se o cliente enviar uma imagem de um produto com defeito,deve registrar a reclamação.
    -Chamar a função `generate_complaint` e fornecer um número de protocolo ao cliente.
    """
    user = get_customer(id_user, order_number)

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):

        if (user["protocol_number"] == False):
            user["foto_produto_defeito_enviada"] = True
            user["status_insatisfacao"] = True
            protocol_number = f"PROT-{user['id_cliente']}-{random.randint(10000, 99999)}"
            user["protocol_number"] = protocol_number
            protocol_number = user["protocol_number"]
            return f"Sucesso!{user['nome']}, Sua solicitação foi registrada sobre o pedido {order_number} e o numero do protocolo é '{protocol_number}'"

        return f"Erro:{user['nome']}, não foi possível registrar sua reclamação"



def generate_discount_coupon(id_user: str, order_number: int) -> str:
    """
     -Se o cliente for recorrente ou estiver insatisfeito("cliente_recorrente" == True ou "status_insatisfacao" == True), pode oferecer um cupom de desconto.
    - Chamar a função `generate_discount_coupon` e enviar o código ao cliente.
    """
    user = get_customer(id_user, order_number)

    if (not user):
        return "Erro: Cliente não encontrado na base de dados."

    if (user):

        if user["cupom_desconto_ativo"] is False:
            # Geramos o cupom
            novo_cupom = f"DESC-{user['id_cliente']}-{random.randint(1000, 9999)}"
            user["cupom_desconto_ativo"] = novo_cupom
            cupom_final = user["cupom_desconto_ativo"]

            return f"Boas notícias, {user['nome']}! Você tem um cupom disponível: {cupom_final}."

        return f"Olá {user['nome']}, no momento não há cupons disponíveis para este perfil."
