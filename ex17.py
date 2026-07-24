""" Classificando o valor da passagem em faixas:

Para cada valor da lista [89.90, 450.00, 1200.00, 305.50, 2999.99], classifique a passagem em faixas: até
200 é "econômica", acima de 200 até 800 é "intermediária", acima de 800 até 2000 é "premium" e acima de
2000 é "executiva". Use if/elif/else dentro de um for e imprima cada valor com sua classificação.

DADOS
valores = [89.90, 450.00, 1200.00, 305.50, 2999.99] """

valores = [89.90, 450.00, 1200.00, 305.50, 2999.99]

for valor in valores: 
    if valor <= 200.00:
        print(f'{valor} - Passagem Econômica')
    elif valor <= 800.00:
        print(f'{valor} - Passagem Intermediária')
    elif valor <= 2000.00:
        print(f'{valor} - Passagem Premium')
    else:
        print(f'{valor} - Passagem Executiva')