""" Filtrando arquivos por extensão:

Uma pasta de ingestão contém os arquivos ["vendas_01.csv", "log.txt", "clientes.CSV",
"backup.csv.gz", "rotas.json"]. Você só quer processar arquivos CSV de verdade, ou seja, cujo nome
termina exatamente em ".csv" (sem diferenciar maiúsculas de minúsculas, e sem pegar o ".csv.gz").
Percorra a lista e imprima apenas os nomes que atendem à regra.

DADOS
arquivos = ["vendas_01.csv", "log.txt", "clientes.CSV", "backup.csv.gz", "rotas.json"] """

arquivos = ["vendas_01.csv", "log.txt", "clientes.CSV", "backup.csv.gz", "rotas.json"]

for i in range (len(arquivos)):
    arquivos[i] = arquivos[i].lower()

csvs = [
    arquivo
    for arquivo in arquivos
    if (arquivo.endswith(".csv")) == True
]

print(csvs)