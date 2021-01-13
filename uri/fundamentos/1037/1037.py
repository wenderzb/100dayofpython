entrada = float(input())
if 0<= entrada <= 25:
    print('Intervalo [0,25]')
if 25< entrada <= 50:
    print('Intervalo (25,50]')
if 50< entrada <= 75:
    print('Intervalo (50,75]')
if 75< entrada <= 100:
    print('Intervalo (75,100]')
if entrada >100 or entrada<0:
    print('Fora de intervalo')