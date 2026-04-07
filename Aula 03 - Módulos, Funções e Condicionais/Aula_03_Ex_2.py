#Faça um programa que leia um número, e informe se ele é par ou impar
def par_ou_impar(numero):
    numero %= 2
    if numero == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
num = int(input("Digite um número: "))
par_ou_impar(num)