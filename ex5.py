""" Ticket médio a partir de entrada do usuário:

Peça ao usuário, com input(), o valor total faturado no dia e a quantidade de vendas realizadas. Lembre-se
de que input() sempre retorna texto: converta o total para decimal (float) e a quantidade para inteiro. Calcule
o ticket médio (total dividido pela quantidade), arredonde para 2 casas e imprima com f-string no formato
Ticket médio: R$ X.

Conceitos: input(), conversão de tipos, round(), operadores """

faturamento_total = float(input('Digite o valor total faturado no dia:'))
quantidade_vendas = int(input('Digite a quantidade de vendas realizadas:'))

if quantidade_vendas > 0:

    ticket_medio = round((faturamento_total/quantidade_vendas), 2)
    print(f'Ticket médio: R$ {ticket_medio}')

else:
    print('A quantidade de vendas deve ser maior que 0')