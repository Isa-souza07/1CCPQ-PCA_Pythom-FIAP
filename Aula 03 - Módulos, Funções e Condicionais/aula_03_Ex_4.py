'''Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a
média alcançada pelo aluno e apresentar:
▪ A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
▪ A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
▪ A mensagem "Reprovado", se a média for menor que cinco.'''

n1 = float(input('Informe a N1 do aluno: '))
n2 = float(input('Informe a N2 do aluno: '))
n3 = float(input('Informe a N3 do aluno: '))
n4 = float(input('Informe a N4 do aluno: '))

media = (n1+n2+n3+n4)/4
if media >=7:
    print("O alun está aprovado!")
elif media >=5 and media <7:
    print("O aluno está em recuperação")
else:
    print("O aluno está reprovado")


