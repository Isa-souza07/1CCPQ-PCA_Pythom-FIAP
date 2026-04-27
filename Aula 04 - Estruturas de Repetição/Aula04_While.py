cp = 0
while cp < 10:
    cp += 1
    if cp == 3:
        continue #se o contador for 3, então ignora-se o que etá em baixo e pula para próxima
    if cp == 7:
        break
    print(f"Produto {cp}")
    #cp += 1

print("")

#while descrescente de 4 até 1
i = 4
while i > 0:
    print(f"Produto {i}")
    i -= 1