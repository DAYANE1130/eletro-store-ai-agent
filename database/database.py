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


def get_customer(id_user: str | None, num_order: int | None) -> Optional[Dict[str, Any]]:
    for dados in customers.values():

        if id_user and str(dados["id_cliente"]) == str(id_user):
            return dados
        if (num_order and dados["num_pedido"] == num_order):
            return dados
        