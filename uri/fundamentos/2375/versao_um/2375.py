diametro_bola = input()
caixa = []
altura_caixa,largura_caixa,profundidade_caixa=input().split()
caixa.append(altura_caixa)
caixa.append(largura_caixa)
caixa.append(profundidade_caixa)
situacao = "S"

for item in range(3):
    if int(diametro_bola) >= int(item):
        situacao = "S"
    else:
        situacao = "N"
        break 

print(situacao)
        
        

