# Dada uma lista de números, crie uma função que retorne os três números mais frequentes em ordem decrescente de frequência. 
# Se houver empates, ordene pelo valor numérico.
# Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
# Saída: [2, 1, 4]


# ------------------ DUVIDA ------------------

lista = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5] 

def numeros_frequentes(lista):
    frequencia = []
    for numero in lista:
        count = lista.count(numero)
        frequencia.append(count)
    return frequencia

resultado = numeros_frequentes(lista)
print(resultado)
