senha_padrao = "2002"

while True:
    senha = input("")
    if senha == senha_padrao:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")