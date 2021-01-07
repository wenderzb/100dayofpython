entrada = input("")

alfabeto = ["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","U","V","W","X","Y","Z"]
resultado = 0

for item in alfabeto:
    resultado+=1
    if item == entrada:
        print(resultado)

