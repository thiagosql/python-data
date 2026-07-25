""" Manipulando uma lista de preços:

Parta da lista precos = [120.0, 350.0, 89.9, 780.0]. Faça, em ordem: adicione o preço 210.0 ao final;
imprima o preço mais caro e o mais barato usando as funções apropriadas; imprima os dois primeiros
preços usando fatiamento (slicing); e imprima em qual índice está o valor 89.9. Comente com print cada
resultado.

DADOS
precos = [120.0, 350.0, 89.9, 780.0]
 """

precos = [120.0, 350.0, 89.9, 780.0]

precos.append(210.0)

print(f'O maior preço da lista é de R$ {max(precos)}')
print(f'O menor preço da lista é de R$ {min(precos)}')
print(f'Os dois primeiros elementos da lista são: {precos[1:3]}')
print(f'O valor de R$ 89.90 está na posição {precos.index(89.9)} da lista')