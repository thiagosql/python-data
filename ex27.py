""" Atualizando o cadastro de um cliente:

Parta do dicionário cliente = {"id": 1007, "nome": "Bruno", "milhas": 24000}. Faça: adicione a chave
"cidade" com valor "Belo Horizonte"; atualize "milhas" somando 5000 às milhas atuais; e remova a
informação que não deveria estar lá, imaginando que "nome" precise ser corrigido para "Bruno Lima".
Imprima o dicionário após cada alteração.

DADOS
cliente = {"id": 1007, "nome": "Bruno", "milhas": 24000} """

cliente = {"id": 1007, "nome": "Bruno", "milhas": 24000}

cliente["cidade"] = "Belo Horizonte"
print(cliente)
cliente["milhas"] = cliente["milhas"] + 5000
print(cliente)
del cliente["nome"]
print(cliente)
cliente["nome"] = "Bruno Lima"
print(cliente)