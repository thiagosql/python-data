""" Convertendo valor monetário em número:

Um valor veio como texto no padrão brasileiro: "R$ 1.234,50". Você precisa transformá-lo no número
decimal 1234.50 para poder somar. Faça a limpeza usando métodos de string em sequência: remova o "R$
", remova o ponto de milhar e troque a vírgula decimal por ponto. Ao final, converta para float e imprima o
número resultante mais o seu type() para confirmar que virou número.

DADOS
bruto = "R$ 1.234,50"

Conceitos: replace(), strip(), conversão float, type() """

bruto = "R$ 1.234,50"

bruto = bruto.replace("R$", ' ').replace(".", "").replace(",", ".")
bruto = bruto.strip()
bruto = float(bruto)

print(bruto, type(bruto))