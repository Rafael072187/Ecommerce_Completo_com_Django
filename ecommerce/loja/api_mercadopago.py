import mercadopago
import os
from django.conf import settings
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
MERCADOPAGO_TOKEN = os.getenv("MERCADOPAGO_TOKEN")

def criar_pagamento(itens_pedido, link_local):
    sdk = mercadopago.SDK(MERCADOPAGO_TOKEN)

    # se o ngrok estiver ativo, usa o link dinâmico
    site_url = os.getenv("NGROK_URL", link_local)

    itens = [{
        "title": item.item_estoque.produto.nome,
        "quantity": int(item.quantidade),
        "unit_price": float(item.item_estoque.produto.preco),
    } for item in itens_pedido]

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": f"{site_url}/finalizarpagamento/",
            "pending": f"{site_url}/finalizarpagamento/",
            "failure": f"{site_url}/finalizarpagamento/",
        },
        "notification_url": f"{site_url}/finalizarpagamento/",
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento
