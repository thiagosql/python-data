""" Somando o faturamento de um dicionário:

Dado o faturamento por rota {"GRU-SDU": 12500.0, "CGH-BSB": 8300.0, "GIG-CNF": 4100.0}, calcule o
faturamento total somando apenas os valores do dicionário. Use o método values() em conjunto com sum().
Imprima o total e também o faturamento médio por rota (total dividido pela quantidade de rotas,
arredondado para 2 casas).

DADOS
fat = {"GRU-SDU": 12500.0, "CGH-BSB": 8300.0, "GIG-CNF": 4100.0}
"""

fat = {"GRU-SDU": 12500.0, "CGH-BSB": 8300.0, "GIG-CNF": 4100.0}

fat_total = sum(fat.values())
fat_rota = fat_total/len(fat)

print(f'O faturamento total foi de R$ {fat_total}')
print(f'Já o faturamento médio por rota foi de R$ {fat_rota}')
