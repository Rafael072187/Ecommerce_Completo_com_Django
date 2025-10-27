from django.db.models import Max, Min

def filtrar_produtos(produtos, filtro):
    if filtro:
        if "-" in filtro:
            categoria, tipo = filtro.split("-")
            produtos = produtos.filter(tipo__slug=tipo, categoria__slug=categoria)
        else:
            produtos = produtos.filter(categoria__slug=filtro)
    return produtos

def preco_minimo_maximo(produtos):
    if not produtos:
        return 0, 0

    # se for queryset
    if hasattr(produtos, "aggregate"):
        maximo = produtos.aggregate(Max("preco"))["preco__max"]
        minimo = produtos.aggregate(Min("preco"))["preco__min"]
    else:
        # se for lista
        precos = [p.preco for p in produtos if hasattr(p, "preco")]
        maximo = max(precos) if precos else 0
        minimo = min(precos) if precos else 0

    return round(minimo, 2), round(maximo, 2)


def ordenar_produtos(produtos, ordem):
    if ordem == "MenorPreco":
        produtos = produtos.order_by("preco")
    elif ordem == "MaiorPreco":
        produtos = produtos.order_by("-preco")
    elif ordem == "MaisVendidos":
        lista_produtos = []
        for produto in produtos:
            lista_produtos.append((produto.total_vendas(), produto))
        lista_produtos = sorted(lista_produtos, key=lambda x: x[0], reverse=True)
        produtos = [item[1] for item in lista_produtos]
    return produtos