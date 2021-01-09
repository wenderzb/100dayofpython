while True:
    nota_um = input("")
    nota_dois = input("")

    if float(nota_um) > 0 and float(nota_dois) > 0 and float(nota_um) < 10 and float(nota_dois) < 10:
        media = (float(nota_um) + float(nota_dois)) / 2
        
        print(f'media = {media:.2f}')
        break
    else:
        print("nota invalida")
