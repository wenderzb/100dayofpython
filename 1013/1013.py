def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a > b:
        if a > c:
            print( '{0} eh o maior'.format(a))    
        else:
            print('{0} eh o maior'.format(c))   
    else:
        if b > c:
            print('{0} eh o maior'.format(b))    
        else:
            print('{0} eh o maior'.format(c))

main()