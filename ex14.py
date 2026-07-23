""" Contando ocorrências em um log:

Dada a linha de log "ERROR conexao ERROR timeout WARN retry ERROR falha", descubra quantas
vezes a palavra "ERROR" aparece usando o método count(). Depois, descubra a posição (índice) da
primeira ocorrência de "WARN" usando find(). Imprima as duas informações com rótulos claros.

DADOS
linha = "ERROR conexao ERROR timeout WARN retry ERROR falha" """

linha = "ERROR conexao ERROR timeout WARN retry ERROR falha"

ocorrencias = linha.count("ERROR")
indice = linha.find("WARN")

print(f'Número de ocorrências da palavra ERROR: {ocorrencias}')
print(F'Índice da string em que se inicia a palavra WARN: {indice}')