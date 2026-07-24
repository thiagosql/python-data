""" Paginação simulada com while:

Uma API retorna resultados em páginas. Simule a leitura: comece em pagina = 1 e vá incrementando
enquanto pagina for menor ou igual a 5. A cada iteração, imprima Lendo página X.... Quando o laço
terminar, imprima Ingestão concluída em 5 páginas. Use while e não use for.
 """

pagina = 1

while pagina <= 5:
    print(f'Lendo página {pagina}...')
    pagina += 1

print('Ingestão concluída em 5 páginas.')