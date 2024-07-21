def main():
    i = 0
    j = 0
    k = 0
    
    m = int(input("Ingrese un entero positivo: "))
    while m <= 0 :
        if(m <= 0): print("Error! m debe ser >0 ")
        m= int(input("Ingrese un entero positivo: "))
        
    for k in range (1, m + 1):
        S1 = 0
        
        for i in range (1, k):
            S2 = 0
            
            if k % i == 0 :
                S1 = S1 + i
            
            for j in range (1, i):
                if i % j == 0:
                    S2 = S2 + j
                    
            print(f"\ni= {i} \tk={k} \tS1={S1} \tS2={S2}")
            
            if S1 == i and S2 == k:
                print(f"Los numeros {i} y {k} son numeros amigos")
            
            
if __name__ == "__main__":
    main()