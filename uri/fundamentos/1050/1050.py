lista_ddd = ["61","71","11","21","32","19","27","31"]
lista_cidades = ["Brasilia","Salvador","Sao Paulo","Rio de Janeiro","Juiz de Fora","Campinas","Vitoria","Belo Horizonte"]
contador = 0
status = "DDD nao cadastrado"
ddd_digitado = int(input())

for item in lista_ddd:
    if ddd_digitado == int(item):
        status = lista_cidades[contador]
        break

    contador += 1

print(status)