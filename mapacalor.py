"""Região: Coluna inicial, linha inicial, coluna final, linha final
Superior (0, 0, 2, 0)
Esquerda (0, 1, 0, 4)
Centro   (1, 1, 1, 4)
Direita  (2, 1, 2, 4)
Inferior (0, 5, 2, 5)

Visualização:

SSS
ECD
ECD
ECD
ECD
III
"""
superior, esquerda, centro, direita, inferior = 0, 0, 0, 0, 0  #Definindo contadores para cada regiao
usuarios = int(input()) #Pegando o número de usuários
for i in range(usuarios): #Um for que se repete para cada usuário
    entrada = [] #Aqui uma lista que é zerada a cada loop do for
    for j in range(6): #Um for que pega 6 linhas de entrada de cada usuário
        entrada.append(list(map(int,input().split()))) #Adicionamos as entradas na lista entrada
    #Saimos do loop, agora que já pegamos as entradas de cada usuário, somamos o número de vezes que cada usuário olhou para cada região.
    superior += sum(entrada[0]) #Aqui a lista recebe a soma de números 1 na primeira linha de cada conjunto de entradas
    esquerda += sum(i[0] for i in entrada[1:5]) #Aqui a lista recebe a soma de números 1 de cada linha da 1 a 4, na primeira coluna
    centro   += sum(i[1] for i in entrada[1:5]) #Aqui a lista recebe a soma de números 1 de cada linha da 1 a 4, na segunda coluna
    direita  += sum(i[2] for i in entrada[1:5]) #Aqui a lista recebe a soma de números 1 de cada linha da 1 a 4, na terceira coluna
    inferior += sum(entrada[5]) #Aqui a lista recebe a soma de números 1 na última linha de cada conjunto de entrada

#Abaixo criamos um dicionário, cada valor do dicionário corresponde a saída desejada como o programa pede, o nome da região em letra minuscula
regioes = {
    'superior' : superior, #Nome da região recebe o número guardado no contador.
    'esquerda' : esquerda,
    'centro'   : centro,
    'direita'  : direita,
    'inferior' : inferior
    }

print(max(regioes, key = regioes.get)) #Função max retorna o maior número associado a região.
