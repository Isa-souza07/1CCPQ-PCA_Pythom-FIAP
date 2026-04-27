def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("Nota inválida, o número deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

nota_A = float(input("Digite a primeira nota: "))
nota_A = verificar_nota(nota_A)
print("")
nota_B = float(input("Digite a segunda nota: "))
nota_B = verificar_nota(nota_B)

media = (nota_A+nota_B)/2
print(media)