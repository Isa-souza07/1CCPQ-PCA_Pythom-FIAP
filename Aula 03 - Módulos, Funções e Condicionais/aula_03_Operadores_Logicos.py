verifica_email = True
verifica_senha = False
verifica_login = verifica_email and verifica_senha #True and False, logo False
print (verifica_login)
if verifica_login: #se for verdadeiro, executa
    print('Entrar no programa')


logica_ou = False or True
print (logica_ou)

negacao = not False
print(negacao)
if not verifica_login:
    print('Verifique seu login e senha')