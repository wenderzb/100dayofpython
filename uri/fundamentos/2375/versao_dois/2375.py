diametro_bola = int(input())
altura, largura, profundidade = input().split()
if diametro_bola <= int(altura) and diametro_bola <= int(largura) and diametro_bola <= int(profundidade):
    print('S')
else:
    print('N')