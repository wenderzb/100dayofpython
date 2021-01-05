#include <stdio.h>

entrada = input("").split()

hora_inicial, minuto_inicial, hora_final, minuto_final = entrada

hora_inicial = int(entrada[0])
minuto_inicial = int(entrada[1])
hora_final = int(entrada[2])
minuto_final = int(entrada[3])

calculo_horas = hora_inicial - hora_final
calculo_minutos = minuto_inicial - minuto_final

duracao_minutos = calculo_minutos * -1 if calculo_minutos <= 0 else 60 - calculo_minutos

if duracao_minutos >= 0:
    duracao_horas =  (24 - (calculo_horas * -1)) - 1 if calculo_horas == 0 else (calculo_horas * -1) - 1 ;
else:
    duracao_horas = 24 - (calculo_horas * -1) if calculo_horas <= 0 else calculo_horas



print('O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(duracao_horas, duracao_minutos))