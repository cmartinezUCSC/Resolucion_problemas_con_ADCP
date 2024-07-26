def main ():
    minutos = 1
    segundos = 1
    
    while minutos !=0 or segundos != 0:
        
        while True:
            try:
                minutos,segundos = map(int, input("Ingrese tiempos en mm ss (0 0 para salir) : ").split())
                if minutos < 0 or segundos < 0:
                    print("\n Ha ingresado un valor invalido, debe ser >= 0. Reintente! \n")
                else:
                    break
            except ValueError :
            
             print("\Entrada invalida. Ingrese dos numeros separados por espacio.\n")
    
    if segundos != 0 or minutos != 0:
        tiempo = segundos+(minutos*60)
        velocidad= 1500/tiempo
        print(f"La velocidad promedio es de : {velocidad:.2f} m/s \n")
        
if __name__ == "__main__":
    main()