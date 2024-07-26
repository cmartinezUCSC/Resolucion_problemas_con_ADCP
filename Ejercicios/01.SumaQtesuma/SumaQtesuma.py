def main():
    suma = 0
    
    while True:
        m = int(input("Ingrese un numero mayor a 0\n"))
        if m > 0:
                break
        else:
            print("Error, debe ser >0")
            
    while True:
        n = int(input("ingrese un numero mayor a 0\n"))
        if n > 0:
            break
        else:
            print("Error, debe ser >0 ")
            
    for i in range( 1, n + 1 ):
        suma = suma + m
    
    print(f"{m} x {n} = {suma}")
    
if __name__ == "__main__":
    main()