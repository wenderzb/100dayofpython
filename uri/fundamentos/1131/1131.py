total_partidas = 0
vitoria_gremio = 0
vitoria_inter = 0
empate = 0
resultado_campeao = ""

while True:
    try:
        entradas = input().split(" ")
        inter, gremio = entradas
        if int(inter) > int(gremio):
            vitoria_inter += 1
        else:
            vitoria_gremio += 1

        total_partidas += 1
        print("Novo grenal (1-sim 2-nao)")
        nova_entrada = int(input())

        if nova_entrada == 2:
            
            empate = total_partidas - (vitoria_gremio + vitoria_inter)
            
            if vitoria_gremio > vitoria_inter:
                resultado_campeao = "Gremio venceu mais"
            elif vitoria_inter > vitoria_gremio:
                resultado_campeao = "Inter venceu mais"
            else:
                resultado_campeao = "Nao houve vencedor"

            break
    except EOFError:
        break

print("{0} grenais".format(total_partidas))
print("Inter:{0}".format(vitoria_inter))
print("Gremio:{0}".format(vitoria_gremio))
print("Empate:{0}".format(empate))
print("{0}".format(resultado_campeao))