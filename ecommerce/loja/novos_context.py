from .models import Pedido, ItensPedido, Cliente, Categoria, Tipo

def carrinho(request):
    quantidade_produtos_carrinho = 0
    cliente = None

    # Evita erro quando o user logado não tem Cliente
    if request.user.is_authenticated:
        try:
            cliente = request.user.cliente
        except Cliente.DoesNotExist:
            cliente = Cliente.objects.create(usuario=request.user, email=request.user.email)
    else:
        if request.COOKIES.get("id_sessao"):
            id_sessao = request.COOKIES.get("id_sessao")
            cliente, _ = Cliente.objects.get_or_create(id_sessao=id_sessao)
        else:
            return {"quantidade_produtos_carrinho": 0}

    pedido, _ = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        quantidade_produtos_carrinho += item.quantidade
    return {"quantidade_produtos_carrinho": quantidade_produtos_carrinho}


def categorias_tipos(request):
    categorias_navegacao = Categoria.objects.all()
    tipos_navegacao = Tipo.objects.all()
    return {"categorias_navegacao": categorias_navegacao, "tipos_navegacao": tipos_navegacao}
