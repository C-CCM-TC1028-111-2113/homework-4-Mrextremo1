
def main():
    #escribe tu código abajo de esta línea
    n = int(input("Enter the index: "))
    i = 1
    f1 = 0
    f2 = 1
    x = 1
    while i <= n or n == 0: 
        if i > n:
            x = f1
            break
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
