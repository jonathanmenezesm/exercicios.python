# Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas notas, 
# crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do aluno e sua média de notas.
# Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
# Saída: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

alunos_notas = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]} #definiçaõ do dicionario

def media_notas(alunos_notas): #Esta é a função que vai receber meu dicionario como parametro.
    medias = [] #lista vazia onde sera retornado o nome do aluno e a media das notas.
    for aluno, notas in alunos_notas.items(): #loop de repitação que lê e executa o bloco de código para cada item do dicionario.
        media = sum(notas) / len(notas) #variavel media que recebe a soma das notas(sum) do aluno dividido pela quantidade(len) de notas.
        medias.append((aluno, round(media, 2))) #append é um metodo que adiciona um item ao final da lista. Round foi um método encontrado para diminuir as casas decimais.
    return medias 

resultado = media_notas(alunos_notas) #variavel que recebe a função para ser printada.
print(resultado)
        