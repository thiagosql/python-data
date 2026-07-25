""" Ordenando clientes por milhas:

Você tem uma lista de dicionários, cada um representando um cliente. Ordene a lista pela quantidade de
milhas, do maior para o menor, usando sorted() com uma função lambda na chave key. Imprima o resultado
ordenado, um cliente por linha, no formato Nome: X milhas.

DADOS
clientes = [
 {"nome": "Ana", "milhas": 24000},
 {"nome": "Bruno", "milhas": 51000},
 {"nome": "Carla", "milhas": 8000},
 {"nome": "Diego", "milhas": 33000},
]
 """

clientes = [
 {"nome": "Ana", "milhas": 24000},
 {"nome": "Bruno", "milhas": 51000},
 {"nome": "Carla", "milhas": 8000},
 {"nome": "Diego", "milhas": 33000},
]

resultado = sorted(clientes, key=lambda cliente: cliente["milhas"], reverse=True)
for cliente in resultado:
    print(f'{cliente["nome"]}: {cliente["milhas"]} milhas')