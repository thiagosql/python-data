""" Arredondando valores monetários:

Um cálculo de rateio gerou os valores [13.6666, 89.1249, 7.005, 250.9950]. Para cada valor, imprima a
versão arredondada para 2 casas decimais usando round(). Em seguida, imprima também um dos valores
arredondado para 0 casas, para comparar o efeito do segundo argumento de round().

Conceitos: round(), listas, for

 """

valores = [13.6666, 89.1249, 7.005, 250.9950]

print('Valores arredondados com duas casas decimais:')

for valor in valores:
    print(round(valor, 2))

print('Valores arredondados com zero casas decimais:')

for valor in valores:
    print(round(valor))