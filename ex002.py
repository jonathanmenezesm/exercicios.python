#Turma - Uma variavel recebendo uma lista com tuplas dentro. Cada tupla tem um nome e uma idade.
turma = [('Joao', 27), ('Maria', 22), ('Pedro', 32), ('Ana', 19)]

#turma_ordenada - Uma variavel recebendo a lista turma ordenada pela idade.
#sorted - Função que ordena uma lista. Estrutura: sorted(lista, key=função).
#key - Parâmetro que recebe uma função lambda que retorna a idade da tupla. Estrutura: key=lambda elemento_escolhido_para_ordenar: elemento_escolhido_para_ordenar[1]. Entre colchetes o índice do elemento escolhido para ordenar.
#lambda - Função anonima que retorna a idade da tupla.
turma_ordenada = sorted(turma, key=lambda idade: idade[1])
print(turma_ordenada)
    





    




        

    