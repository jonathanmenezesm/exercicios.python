# Lista de strings
string = ['java', 'javascript', 'php', 'html', 'css', 'php', 'ruby', 'sql', 'java']

def contagem_frequencia(string):
    contador = {}
    for item in string:
        if item in contador:  
            contador[item] += 1  
        else:
            contador[item] = 1  
    return contador

resultado = contagem_frequencia(string)
print(resultado)