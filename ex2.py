""" Inspecionando os tipos de um registro:

Você recebeu um registro solto de um sistema, com campos de tipos diferentes. Para cada um dos valores
abaixo, imprima o próprio valor seguido do seu tipo, usando type(). A saída de cada linha deve ter o
formato: valor -> tipo. Isso simula a inspeção que se faz antes de decidir como tratar cada coluna.

DADOS
id_cliente = 1007
nome = "Bruno Lima"
ticket_medio = 512.75
ativo = True
tags = ["vip", "recorrente"]

Conceitos: type(), print() """

id_cliente = 1007
nome = "Bruno Lima"
ticket_medio = 512.75
ativo = True
tags = ["vip", "recorrente"]

print(f'{id_cliente} -> {type(id_cliente)}')
print(f'{nome} -> {type(nome)}')
print(f'{ticket_medio} -> {type(ticket_medio)}')
print(f'{ativo} -> {type(ativo)}')
print(f'{tags} -> {type(tags)}')