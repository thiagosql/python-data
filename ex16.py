""" Validação simples de e-mail:

Para cada e-mail da lista ["ana@empresa.com", "bruno.com", "carla@", "diego@x.com.br"], verifique
se ele parece válido com uma regra simples: precisa conter exatamente um "@" e ter pelo menos um "."
depois do "@". Imprima cada e-mail seguido de "válido" ou "inválido". Use operadores de string (in, count) e
split() para a checagem.

DADOS
emails = ["ana@empresa.com", "bruno.com", "carla@", "diego@x.com.br"] """

emails = ["ana@empresa.com", "bruno.com", "carla@", "diego@x.com.br"]

for email in emails: 
    if ((email.count("@") == 1) and (email.find("@") <= email.rfind("."))): 
        print(f'{email} --> Válido')
    else:
        print(f'{email} --> Inválido')