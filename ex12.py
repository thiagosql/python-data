""" Normalizando códigos de aeroporto:

Os códigos IATA de origem e destino vieram bagunçados: [" gru", "Cgh ", "sdu", " GIG "]. O padrão
correto é: sem espaços e todas as letras maiúsculas. Padronize cada código e monte uma nova lista já
limpa, imprimindo-a ao final. O resultado esperado é ['GRU', 'CGH', 'SDU', 'GIG'].

DADOS
codigos = [" gru", "Cgh ", "sdu", " GIG "] """

codigos = [" gru", "Cgh ", "sdu", " GIG "]

iatas = [
    codigo.upper().strip()
    for codigo in codigos
]

print(iatas)