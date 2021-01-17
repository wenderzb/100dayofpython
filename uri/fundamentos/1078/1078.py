numero_digitado = int(input())
tabuada = [1,2,3,4,5,6,7,8,9,10]
for item in tabuada:
    calculo = item * numero_digitado
    print("{0} x {1} = {2}".format(item,numero_digitado,calculo))