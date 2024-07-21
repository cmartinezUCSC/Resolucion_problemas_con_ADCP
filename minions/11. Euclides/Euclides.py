def main():
    m, n=0,0
    
    while True:
        try:
            m, n =map(int, input("Ingrese dos numeros separados por espacio: ").split())
            
            if m != 0 and n != 0:
                if m%n == 0:
                    if m < n:
                            print (m)
                    if n < m:
                            print (n)
                else:
                    while m % n != 0:
                        mod = m % n
                        m = n
                        n = mod
                    print (mod)
                break
            else:
                print("ERROR, deben ser != 0 ")
        except ValueError:
            print ("ERROR, entrada no valida. Ingres numeros enteros")
        

if __name__ == "__main__":
    main()