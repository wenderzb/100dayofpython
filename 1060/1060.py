lista_entrada = []

positivos = 0

for item in range(6):
    lista_entrada.append(int(input()))
    if lista_entrada[item] > 0:
        positivos += 1


print("{0} valores positivos".format(positivos))



