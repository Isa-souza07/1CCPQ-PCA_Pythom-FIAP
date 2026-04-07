#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.
def numeros(num_1, num_2):
    if num_1 == num_2:
        print (f'O número {num_1} é igual a {num_2}.')
    elif num_1 > num_2:
        print(f'O número {num_1} é maior que {num_2}.')
    else:
        print(f'O número {num_2} é maior que {num_1}.')

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite outro número: "))
numeros(num_1, num_2)