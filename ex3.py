""" Cálculo de valor líquido:

Uma passagem custa bruto = 1250.00. Sobre esse valor incide uma taxa de embarque de 78.40 (soma) e
um desconto de fidelidade de 12% aplicado somente sobre o valor bruto (não sobre a taxa). Calcule o valor
final a pagar usando apenas operadores aritméticos e imprima o resultado. Deixe claro no print o valor
bruto, o desconto em reais e o valor final.

Conceitos: operadores aritméticos, print() """

custo_bruto = 1250.00
taxa_embarque = 78.40
desconto_fidelidade = round(((custo_bruto - taxa_embarque) * 0.12), 2)
valor_final = round((custo_bruto - desconto_fidelidade), 2)

print(f'O valor final a ser pago pela passagem é de R$ {valor_final}. Houve um desconto de R$ {desconto_fidelidade} sobre o valor bruto, dado por R$ {custo_bruto}')