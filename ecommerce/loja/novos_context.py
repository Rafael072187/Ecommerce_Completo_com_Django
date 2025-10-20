from .models import Pedido, ItensPedido

def carrinho(request):
    quantidade_produtos_carrinho = 0
    cliente = None
    pedido = None

    if request.user.is_authenticated:
        try:
            cliente = request.user.cliente
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
            itens_pedido = ItensPedido.objects.filter(pedido=pedido)
            for item in itens_pedido:
                quantidade_produtos_carrinho += item.quantidade
        except Exception as e:
            print("Erro ao acessar carrinho autenticado:", e)
    else:
        print("Usuário não logado — carrinho vazio")

    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}
