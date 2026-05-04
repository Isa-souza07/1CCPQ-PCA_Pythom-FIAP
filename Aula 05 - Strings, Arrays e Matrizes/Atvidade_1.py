'''Dado um conjunto de nomes de quatro pessoas, escreva um algoritmo que imprima todas as possíveis
duplas que podem ser formadas.
Primeiro, crie um vetor e coloque quatro nomes nele.
A seguir, exiba as possíveis duplas'''
nomes = ["Ana", "Maria", "Enzo", "Leo", "Iris"]
for i in range(len(nomes)):
    # print(i)
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])
        #print(i, j)
