import random

def main():
    numero = random.randint(1, 100)
    leido = 0
    
    while leido != numero:
        print("Ingresa un numero:")
        leido = int(input())
        
        if numero < leido:
            print("El numero a adivinar es menor que el que ingresaste.")
        elif numero > leido:
            print("El numero a adivinar es mayor que el que ingresaste")
    print("¡Felicidades, has adivinado!")

if __name__=="__main__":
    main()