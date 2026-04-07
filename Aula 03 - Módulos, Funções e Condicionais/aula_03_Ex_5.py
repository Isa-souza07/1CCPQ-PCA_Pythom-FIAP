'''Faça um programa que leia 2 valores inteiros (A e B).
 A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando
se os valores lidos são múltiplos entre si.
Dica:
▪ Como que eu sei que 2 números são ou não são múltiplos um do outro?
▪ Conjunto dos Múltiplos de 2 = {2, 4, 6, 8, 10, ...}
▪ Então se observa que os múltiplos de um número são divisíveis por esse número, então o resto dessa
divisão será 0.'''
def multiplos(num1, num2):
    if num1 % num2 == 0:
        print(f'O número {num1} é múltiplo de {num2}.')
    elif num2 % num2 == 0:
        print(f'O número {num2} é múltiplo de {num1}.')
    else:
        print(f'O número {num2} não é múltiplo de {num1}.')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
multiplos(num1, num2)
