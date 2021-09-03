def main():
    #escribe tu código abajo de esta línea
    n = int(input("ingresa un numero"))
    for i in range(1, n+1):
        if i % 2 == 0:
            print(str(i) + "-%")
        else:
            print(str(i) + "-#")


if __name__=='__main__':   
    main()
