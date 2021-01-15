segundos = int(input())
total_horas = segundos // 60 ** 2
segundos = segundos - total_horas * 60 ** 2

total_minutos = segundos // 60
segundos = segundos - total_minutos * 60

total_segundos = segundos

print('{}:{}:{}'.format(total_horas, total_minutos, total_segundos))