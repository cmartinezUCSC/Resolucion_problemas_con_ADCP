def main ():
    n = -1
    
    while n < 0:
        try:
         
         n = float(input("Ingrese un numero mayor o igual a 0:"))
         if n < 0:
            print("Error, debe ser >= 0")
        except ValueError:
            print("Error, ingrese un numero valido.")
    
    t0 = 0
    t1 = 1
    
    if n == 0:
        print(f"t0={t0}")
    else:
        print(f"t0={t0}")
        print(f"t1={t1}")
        
        for i in range(2, int(n) + 1):
            tn= t0 + t1
            t0, t1 = t1,tn
            print(f"{i}={tn}")
            
if __name__ == "__main__":
    main()