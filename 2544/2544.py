while True:
    try:
        entrada = int(input())
        resultado = 0
        while(entrada > 1):
            entrada //= 2
            resultado += 1
        print(resultado)
    except EOFError:
        break