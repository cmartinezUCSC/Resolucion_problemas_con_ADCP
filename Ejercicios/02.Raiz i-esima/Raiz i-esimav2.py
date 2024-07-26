import math

def main():
    numero,i,raiz = 0.0, 0.0, 0.0
    
    while True:
        try:
            numero = float(input())
            if numero < 0:
                print("Error,debe ser >= 0")
            else:
                break
        except ValueError:
            print("ERROR, entrada no valida. Ingrese un numero")
            
    while True:
        try:
            i = float(input())
            if i<= 0:
                print("ERROR, debe ser > 0")
            else:
                break
        except ValueError:
            print("ERROR, entrada no valida, ingrese un numero")
    
    raiz= numero ** ( 1 / i )
    
    print("{:.3f}".format(raiz))
    
if __name__ == "__main__":
    main()