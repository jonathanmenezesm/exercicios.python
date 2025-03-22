# Escreva uma função que recebe uma palavra e retorna True se for um palíndromo (ou seja, se
# pode ser lida da mesma forma de trás para frente) e False caso contrário.
# Exemplo:
# entrada = "radar"
# Saída: True

print("Vamos verificar se a palavra é um palindromo?")
palavra = input('digite a palavra: ') #define uma entrada de dados para o usuario verificar se a palavra é um palindromo.

def palindromo(palavra):    
    if palavra == palavra[::-1]: #se a palavra for igual a ela mesma ao contrário
        return True
    else:
        return False
    
resultado = palindromo(palavra) #variavel que recebe a função para ser printada.

#aqui é um mero capricho para dizer se a palavra é ou não um palindromo. 
if resultado == True:
    print(f'A palavra {palavra} é um palindromo, pois, a palavra original é: "{palavra}" e ao contrário fica exatamente igual.')
else:
    print(f'A palavra {palavra} não é um palindromo, pois, a palavra original é: {palavra}, ao contrário fica: {palavra[::-1]}')

    