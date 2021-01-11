numero_teste=int(input())
while numero_teste > 0:
    figurinha_ricardo,figurinha_vicente = map(int,input().split())
    def mdc(a,b):
        if b == 0:
            return a
        return mdc(b, a % b)
    print(mdc(figurinha_ricardo,figurinha_vicente))
    numero_teste -= 1