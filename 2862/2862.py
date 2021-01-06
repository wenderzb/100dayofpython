entrada = int(input())
rodada = 0

while(rodada < entrada):
    nivel_poder = int(input())
    if nivel_poder > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")

    rodada+=1    
    