""" Contando vendas por companhia:

Dada a lista de companhias de cada venda ["LATAM", "GOL", "LATAM", "AZUL", "GOL", "LATAM",
"AZUL"], monte um dicionário que conte quantas vendas cada companhia teve. Percorra a lista e, para
cada companhia, incremente sua contagem no dict (criando a chave se ainda não existir). Imprima o
dicionário final, que deve ser {'LATAM': 3, 'GOL': 2, 'AZUL': 2}.

DADOS
cias = ["LATAM", "GOL", "LATAM", "AZUL", "GOL", "LATAM", "AZUL"]
 """

cias = ["LATAM", "GOL", "LATAM", "AZUL", "GOL", "LATAM", "AZUL"]

vendas_cia = {}

for cia in cias:
    if cia not in vendas_cia:
        vendas_cia[cia] = 0
    vendas_cia[cia] += 1

print(vendas_cia)