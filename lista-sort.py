# Syntax
# list.sort(reverse=True|False, key=myFunc)
#
# Parameter Values
#
# Parameter 	Description
#
# reverse 	    Opcional. reverse = True irá classificar a lista em ordem decrescente.
#               O padrão é reverso = False
# key 	        Opcional. Uma função para especificar os critérios de classificação

lista = [
    ['p6', 13.67],
    ['p4', 15.17],
    ['p3', 83.07],
    ['p2', 33.66]
]

print(f'\n lista oferecida: {lista}')


def ordenalistaPreco(item):
    return item[1]  # item[0] é o preço e item[1] é o preço


def ordenalistaItem(item):
    return item[0]  # item[0] é o produto e item[0] é o preço


lista.sort(key=ordenalistaPreco)  # Colocar fora do print
print(f'\n lista.sort(key=ordenalistaPreco):\n {lista}')
#
lista.sort(key=ordenalistaItem)  # Colocar fora do print
print(f'\n lista.sort(key=ordenalistaItem):\n {lista}')
#
lista.sort(key=ordenalistaItem, reverse=True)  # Colocar fora do print
print(f'\n lista.sort(key=ordenalistaItem, reverse=True):\n {lista}')
