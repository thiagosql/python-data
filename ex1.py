""" Registro de uma venda:

Crie quatro variáveis para representar uma venda de passagem: id_venda (inteiro, valor 4821), cliente
(texto, "ana souza"), valor (decimal, 389.90) e pago (booleano, True). Depois, usando uma única chamada
de print() com f-string, exiba a frase: Venda 4821 de ana souza no valor de R$ 389.9 (paga: True). Os
valores mostrados devem vir sempre das variáveis, nunca digitados direto no texto.

Conceitos: variáveis, tipos, print(), f-string """

id_venda = int(4821)
cliente = str("ana souza")
valor = float(389.90)
pago = bool(True)

print(f'Venda {id_venda} de {cliente} no valor de {valor} (paga: {pago})')