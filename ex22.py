""" Marcando registros para revisão:

Percorra os valores [100.0, -50.0, 320.0, 0.0, 890.0, -12.5]. Um valor negativo indica erro de estorno mal
registrado e um valor igual a zero indica venda de teste. Para cada valor, imprima: OK se for positivo,
ERRO: negativo se for menor que zero e IGNORAR: teste se for zero.

DADOS
valores = [100.0, -50.0, 320.0, 0.0, 890.0, -12.5]
 """

valores = [100.0, -50.0, 320.0, 0.0, 890.0, -12.5]

for valor in valores:
    if valor > 0:
        print(f'{valor} - OK')
    elif valor < 0:
        print(f'{valor} - ERRO: negativo')
    else:
        print(f'{valor} - IGNORAR: teste')