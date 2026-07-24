""" Contando vendas aprovadas:

Dada a lista de status de pagamento ["pago", "pendente", "pago", "cancelado", "pago", "estornado",
"pago"], conte quantas vendas estão com status "pago" e quantas não estão. Percorra com for, use if/else
e imprima as duas contagens com rótulos.

DADOS
status = ["pago", "pendente", "pago", "cancelado", "pago", "estornado", "pago"] """

status = ["pago", "pendente", "pago", "cancelado", "pago", "estornado", "pago"]

pago = 0
nao_pago = 0

for venda in status: 
    if venda == "pago": 
        pago += 1
    else:
        nao_pago += 1

print(f'Foram encontradas {pago} vendas com status "pago" e {nao_pago} vendas com status diferente de pago.')