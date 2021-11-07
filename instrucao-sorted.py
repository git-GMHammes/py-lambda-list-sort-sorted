#
# sorted(iterable, key=key, reverse=reverse)
#
# Parameter 	Description
#
# iterable 	    Obrigatório. A sequência para classificar, listar, dicionário, tupla etc.
# key 	        Opcional. Uma função a ser executada para decidir o pedido. O padrão é nenhum
# reverse 	    Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
#
lista = [
    ['p6', 13.67],
    ['p4', 15.17],
    ['p3', 83.07]
]

print(f'\n lista recebida: {lista}')
print(f'\n {sorted(lista)}')
print(f'\n {sorted(lista, key=lambda i: i[1], reverse=True)}')
