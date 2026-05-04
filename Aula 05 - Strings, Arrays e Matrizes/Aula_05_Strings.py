texto = "FIAP Paulista"
print(texto[0]) #acessa o primeiro caractere da string
tamanho = len(texto)
print(tamanho) #espaço em branco conta
for i in range(tamanho):
    print(f"texto[{i}] = {texto[i]}")
for c in texto:
    print(c)