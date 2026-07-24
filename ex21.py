""" Maior venda sem usar max():

Encontre a maior venda da lista [780.25, 1200.0, 350.5, 2999.99, 890.0] percorrendo com for e comparando
manualmente cada valor a um "maior até agora". Imprima o valor máximo encontrado. Não use a função
max().

DADOS
vendas = [780.25, 1200.0, 350.5, 2999.99, 890.0] """

vendas = [780.25, 1200.0, 350.5, 2999.99, 890.0]

maior_valor = vendas[0]

for venda in vendas:
    if venda > maior_valor:
        maior_valor = venda

print(f'A maior venda encontrada foi no valor de R$ {maior_valor}')