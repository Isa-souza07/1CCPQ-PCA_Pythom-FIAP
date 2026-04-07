#Receba a idade e indique se o voto é opcional
def pode_votar(idade):
    if idade < 16:
        print("Não pode votar.")
    elif (idade>=16 and idade<18) or idade>70:
        print("O voto é opcional.")
    else:
        print("O voto é obrigatório.")

pode_votar(int(input('Informe sua idade: ')))

#Forma sem função
'''idade = int(input('Informe sua idade: '))
if idade < 16:
    print("Não pode votar.")
elif (idade >=16 and idade <18) or idade>70:
    print("O voto é opcional.")
else:
    print("O voto é obrigatório.")'''
