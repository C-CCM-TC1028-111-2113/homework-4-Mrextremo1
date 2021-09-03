
def main():
    #escribe tu código abajo de esta línea
    n = int(input())
    i = 1
    f1 = 0
    f2 = 1
    if n == 0:
        x = f1
    elif n == 1:
        x = f2
    while i <= n and n > 1: 
        f1 = f1 + f2
        i = i + 1
        if i == n:
            x = f1
            break
        f2 = f1 + f2
        i = i + 1
        if i == n:
            x = f2
            break
    print(x)
    

        

if __name__=='__main__':
    main()
