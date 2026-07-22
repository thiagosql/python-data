""" Acumulando o faturamento:

Comece com total = 0.0. Você recebe as vendas do dia em quatro momentos: 1200.00, depois 350.50,
depois 890.00 e por fim 45.90. Some cada uma ao acumulador usando o operador de atribuição composto
(+=), imprimindo o total parcial após cada soma. No fim, imprima o total consolidado.

Conceitos: operadores de atribuição, print() """

total = 0.0

for i in range (4):
    valor_venda = float(input("Digite o valor da nova venda: "))
    total += valor_venda
    if i == 3:
        print(f'Valor vendido no dia: {total}')
    else:
        print(f'Valor parcial das vendas diárias: {total}')

