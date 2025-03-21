lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def soma_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

resultado = soma_pares(lista)
print('A soma dos pares é: ', resultado)

