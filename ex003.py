string = 'java'

def contagem_caracteres(string):
    contador = {} #define um dicionário vazio
    for caracter in string:  #para cada letra na string :(faça); nada mais seria do que percorrer a string com as condições abaixo.
        if caracter in contador: #se a letra já estiver no dicionário
            contador[caracter] += 1  # Incrementa a contagem 
        else:
            contador[caracter] = 1  # Adiciona a letra ao dicionário com contagem 1
    return contador #retorna o dicionário com os valores atualizados

resultado = contagem_caracteres(string)
print(resultado)
