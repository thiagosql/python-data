""" Quebrando uma linha de CSV:

Você recebeu uma linha de arquivo no formato CSV como uma única string: "4821;Ana
Souza;GRU;389.90;pago", onde o separador é ponto e vírgula. Separe a linha em uma lista de campos e
imprima cada campo com seu índice, no formato 0: 4821, 1: Ana Souza, e assim por diante. Depois imprima
especificamente o campo de valor (índice 3).

Conceitos: split(), listas, indexação """

linha = "4821;Ana Souza;GRU;389.90;pago"

campos = linha.split(";")

for i in range(len(campos)):
    print(f'{i}: {campos[i]}')

print(f'Campo com índice 3: {campos[3]}')