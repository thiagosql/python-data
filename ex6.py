""" Comparando com a meta:

A meta diária de vendas é meta = 50000.00 e o realizado foi realizado = 47320.50. Usando apenas
operadores relacionais, crie e imprima três variáveis booleanas: bateu_meta (realizado maior ou igual à
meta), ficou_abaixo (realizado menor que a meta) e faltou_pouco (a diferença para a meta é menor que
5000). Imprima as três com rótulos claros.

Conceitos: operadores relacionais, booleanos """

meta = 50000.00
realizado = 47320.50

bateu_meta = (realizado >= meta)
ficou_abaixo = (realizado < meta)
faltou_pouco = (((meta - realizado) > 0) and ((meta - realizado) < 5000.00))

print(f'A meta foi batida? {bateu_meta}')
print(f'O valor vendido fixou abaixo da meta? {ficou_abaixo}')
print(f'Faltou pouco para bater a meta? {faltou_pouco}')