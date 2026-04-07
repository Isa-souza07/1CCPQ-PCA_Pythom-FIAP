#Função com parâmetro e sem retorno
'''def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem-vindo!")

#boas_vindas("Alexandre")
nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado) '''

#Função com parâmetro e retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(1, 2))
#OU
resultado_soma = soma(1, 2)
print(resultado_soma)