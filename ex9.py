""" Padronizando nomes de clientes:

Os nomes chegam do formulário com espaços sobrando e capitalização inconsistente: [" ana souza ",
"BRUNO LIMA", " Carla ", "díEGO ramos "]. Para cada nome, remova os espaços das pontas, deixe em
formato de nome próprio (primeira letra de cada palavra maiúscula) e imprima o resultado. Ao final, todos
devem sair limpos, como Ana Souza.

DADOS:
nomes = [" ana souza ", "BRUNO LIMA", " Carla ", "diego ramos "]

Conceitos: strip(), title(), for """

nomes = [" ana souza ", "BRUNO LIMA", " Carla ", "diego ramos "]

for i in range(len(nomes)): 
    nomes[i] = nomes[i].strip()
    nomes[i] = nomes[i].title()

for nome in nomes: 
    print(nome)