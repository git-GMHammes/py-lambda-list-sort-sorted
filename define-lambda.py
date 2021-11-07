#
# Função que retorna a Lambda
#
def minhaFuncao(n):
    return lambda a: a * n  # lambda a: a = valorDuplicado(11)


valorDuplicado = minhaFuncao(2)
print(f'\n def minhaFuncao(n):')
print(f'     return lambda a: a * n')
print(f'\n valorDuplicado = minhaFuncao(2): {valorDuplicado(11)}')
print(f'\n {" - -" * 10}')


def exFuncao(val, n):
    return outraFuncao(val, n)


def outraFuncao(val, n):
    return val * n


print(f'\n def exFuncao(val, n):')
print(f'    return outraFuncao(val, n)\n \n')
print(f'\n def outraFuncao(val, n):')
print(f'     return val * n ')
print(f'\n exFuncao(val, n): outraFuncao(val, n): {exFuncao(11, 2)} \n')
