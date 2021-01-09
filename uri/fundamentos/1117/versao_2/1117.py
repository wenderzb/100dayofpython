numero_nota = 0
total_nota = 2
media = 0
while numero_nota < total_nota:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        numero_nota = numero_nota + 1
        media = media + nota
    if nota < 0 or nota > 10:
        print('nota invalida')
media = media / 2
print('media = {:.2f}'.format(media))