from typing import Dict, Any, Optional

customers: Dict[str, Dict[str, Any]] = {
    "cliente_01": {
        "id_cliente": "1",
        "nome": "Ana Silva",
        "num_pedido": 1001,
        "status_pedido": "Entregue",
        "valor_total": 150.00,
        "total_pedidos_historico": 8,
        "cliente_recorrente": True,
        "status_insatisfacao": False,
        "comprovante_pagamento_enviado": True,
        "foto_produto_defeito_enviada": False,
        "protocol_number": False,
        "cupom_desconto_ativo": False
    },
    "cliente_02": {
        "id_cliente": "2",
        "nome": "Bruno Lima",
        "num_pedido": 1002,
        "status_pedido": "Processando",
        "valor_total": 151.00,
        "total_pedidos_historico": 1,
        "cliente_recorrente": False,
        "status_insatisfacao": True,
        "comprovante_pagamento_enviado": False,
        "foto_produto_defeito_enviada": True,
        "protocol_number": False,
        "cupom_desconto_ativo": False
    },
    "cliente_03": {
        "id_cliente": "3",
        "nome": "Carla Diniz",
        "num_pedido": 1003,
        "status_pedido": "Enviado",
        "valor_total": 152.00,
        "total_pedidos_historico": 5,
        "cliente_recorrente": True,
        "status_insatisfacao": False,
        "comprovante_pagamento_enviado": True,
        "foto_produto_defeito_enviada": False,
        "protocol_number": False,
        "cupom_desconto_ativo": "FRETE20"
    },
    "cliente_04": {
        "id_cliente": "4",
        "nome": "Davi Rocha",
        "num_pedido": 1004,
        "status_pedido": "Aguardando Pagamento",
        "valor_total": 153.00,
        "total_pedidos_historico": 0,
        "cliente_recorrente": False,
        "status_insatisfacao": False,
        "comprovante_pagamento_enviado": False,
        "foto_produto_defeito_enviada": False,
        "protocol_number": False,
        "cupom_desconto_ativo": False
    },
    "cliente_05": {
        "id_cliente": "5",
        "nome": "Elena Sampaio",
        "num_pedido": 1005,
        "status_pedido": "Em Trânsito",
        "valor_total": 154.00,
        "total_pedidos_historico": 12,
        "cliente_recorrente": True,
        "status_insatisfacao": True,
        "comprovante_pagamento_enviado": True,
        "foto_produto_defeito_enviada": False,
        "protocol_number": False,
        "cupom_desconto_ativo": False
    }
}


def list_customers() -> Dict[str, Dict[str, Any]]:
    customers_list = []
    for customer in customers:
        customers_list.append(customer)
    return customers_list

#print('sou a lista de customers', list_customers())
# //['cliente_01', 'cliente_02', 'cliente_03', 'cliente_04', 'cliente_05']


def get_customer(customer_id: str) -> Optional[Dict[str, Any]]:
    for dados in customers.values():

        # 2. Verificamos se o ID e o Número do Pedido coincidem
        if (dados["id_cliente"] == customer_id):
            return dados
#teste de busca de cliente
# print(get_customer("5"))#retorna todos os dados do cliente
