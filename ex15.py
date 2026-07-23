""" Remontando uma linha para exportação:

Você tem os campos de um registro já separados em uma lista: ["4821", "Ana Souza", "GRU", "389.90"].
Monte de volta uma única string no formato CSV usando vírgula como separador, através do método join().
Imprima a linha final. Atenção: join() exige que todos os itens sejam texto.

DADOS
campos = ["4821", "Ana Souza", "GRU", "389.90"] """

campos = ["4821", "Ana Souza", "GRU", "389.90"]

linha = ";".join(campos)

print(linha)