""" Somando com laço explícito:

Sem usar a função sum(), calcule o faturamento total percorrendo a lista [1200.0, 350.5, 890.0, 45.9,
780.25] com um for e um acumulador. Imprima o total ao final. O objetivo aqui é praticar o laço manual
antes de usar os atalhos prontos.

DADOS
vendas = [1200.0, 350.5, 890.0, 45.9, 780.25] """

vendas = [1200.0, 350.5, 890.0, 45.9, 780.25]
total = 0.0

for venda in vendas:
    total += venda

print(f'Valor total vendido: {total}')