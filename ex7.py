""" Elegibilidade para upgrade:

Um cliente ganha upgrade de cabine se: for membro do programa de fidelidade E (tiver mais de 30000
milhas OU ter voado mais de 20 vezes no ano). Dados fidelidade = True, milhas = 24000 e voos_ano =
22, escreva uma única expressão usando operadores lógicos (and, or) que resulte em True ou False e
imprima se o cliente tem direito ao upgrade.

Conceitos: operadores lógicos, booleanos """

fidelidade = True
milhas = 24000 
voos_ano = 22

recebe_upgrade = (fidelidade == True and (milhas >= 30000 or voos_ano >=20))

print(f'O cliente tem direito ao upgrade? {recebe_upgrade}')