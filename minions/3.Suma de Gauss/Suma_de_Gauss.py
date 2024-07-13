def main():
    
    n = int (input("Ingrese un numero"))
    resultado = 0
    
    if n < 1:
        print("Error, debe >=1")
    else:
        for i in range (1, n + 1):
            resultado +=i
            
        print("La suma de los numeros desde 1 hasta {} en: {} ".format(n, resultado))

if __name__=="__main__":
    main()