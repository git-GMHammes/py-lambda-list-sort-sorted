#
# Onde lambda item: item[1], item é a função que recebe o valor
#
lista = [
    ['p6', 13.67],
    ['p4', 15.17],
    ['p3', 83.07],
    ['p2', 33.66]
]

print(f'\n Lista recebida: {lista}')
# Ordenar a lista por valor representado pelo item[1]
lista.sort(key=lambda item: item[1], reverse=True)  # Colocar fora do print
print(f'\n Lista ordenada por key=lambda item: item[1] = Preço: \n {lista} \n')
#
# Ordenar a lista por produto representado pelo chave[0]
lista.sort(key=lambda chave: chave[0], reverse=False)  # Colocar fora do print
print(
    f'\n Lista ordenada por key=lambda chave: chave[0] = Produto: \n {lista} \n'
)
