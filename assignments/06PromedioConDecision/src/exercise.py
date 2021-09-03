def main():
    #escribe tu código abajo de esta línea
    n = 0
    c = 0
    p = 0
    while n >= 0:
        c = c + 1
        p = p + n
        n = float(input())
    print(p/(c-1))


if __name__=='__main__':
    main()
