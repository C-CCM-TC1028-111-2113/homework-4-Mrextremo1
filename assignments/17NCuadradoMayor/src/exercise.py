

def main():
    #Escribe tu código debajo de esta línea
    n = int(input("Escribe un numero : "))
    for i in range(0, n+2):
        if i**2 > n:
            break
    print(i)
if __name__=='__main__':
    main()
