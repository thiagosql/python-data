""" Interrompendo e pulando no laço:

Você está processando registros até encontrar um marcador de fim. Percorra a lista ["350.5", "vazio",
"890.0", "FIM", "45.9"]. Se o item for "vazio", pule para o próximo com continue (não processa). Se for
"FIM", encerre o laço com break. Para os demais, converta para float e some em um acumulador. Ao final,
imprima o total somado antes do "FIM" (deve ser 1240.5).

DADOS
registros = ["350.5", "vazio", "890.0", "FIM", "45.9"]
 """

registros = ["350.5", "vazio", "890.0", "FIM", "45.9"]

total_final = 0

for registro in registros:
    if registro == "FIM":
        break 
    elif registro == "vazio":
        continue 
    else:
        valor = float(registro)
        total_final += valor 

print(f'O valor total vendido foi de R$ {total_final}')