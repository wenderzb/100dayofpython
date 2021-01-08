lista_entrada = []

positivos = 0
negativos = 0
pares = 0
impares = 0 

for item in range(5):
    lista_entrada.append(input())
    resto = int(lista_entrada[item]) % 2

    if resto == 0:
        pares += 1
    else:
        impares += 1


    if int(lista_entrada[item]) > 0:
        positivos += 1
    elif int(lista_entrada[item]) < 0:
        negativos += 1


print("{0} valor(es) par(es)".format(pares))
print("{0} valor(es) impar(es)".format(impares))
print("{0} valor(es) positivo(s)".format(positivos))
print("{0} valor(es) negativo(s)".format(negativos))


