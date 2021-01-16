x = input().split()
a, b, c =x
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    calculo_perimetro = a + b + c
    print('Perimetro = {:.1f}'.format(calculo_perimetro))
else:
    calculo_area = ((a + b) / 2) * c
    print('Area = {:.1f}'.format(calculo_area))