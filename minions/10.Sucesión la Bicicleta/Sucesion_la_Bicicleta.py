def main():
    b0, b1, bn = 2.0, 3.0, 0.0
    i, n= 0, 0
    
    while n < 3:
        n = int(input("Ingrese un numero (debe ser >= 3) : "))
        if n >= 3:
            break
        else:
            print("Error, debe ser >= 3 ")
            
    b0,b1= 2.0, 3.0
    print("{}\n{}".format(b0, b1))
    
    for i in range(1, n - 1):
        bn = (b1 + 1)/b0
        print("{}".format(bn))
        b0, b1 = b1, bn
    

if __name__ == "__main__":
    main()
# devuelve con decimales y en los casos prueba no aparecen con decimales