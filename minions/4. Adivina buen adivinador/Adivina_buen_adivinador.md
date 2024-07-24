# 4. Adivina buen adivinador

#### Dificultad: fácil

## Descripcion

*El jugador P (pensador) piensa en un número comprendido en entre 1 y n. El jugador A trata de adivinarlo por tanteos sucesivos hasta llegar a él. Cada intento debe orientar al jugador A. Suponga que usted dispone de la función rand (n) o azar(n) para generar números aleatorios entre 0 y n-1.*
    

# Solución ADCP

# (A)NÁLISIS
###### Entradas:   Número n del jugador A por cada intento de adivinar. 

###### Proceso mental:

¿Qué es un número aleatorio? ¿Cómo se genera?  Un número aleatorio es un valor numérico que es seleccionado al azar o de manera 
impredecible a partir de un rango o conjunto de valores posibles. La generación de números aleatorios es fundamental en diversas áreas, 
como la estadística, la programación, la simulación, los juegos, entre otros campos.

Es esencial que los números aleatorios sean impredecibles y equitativos, es decir, que tengan la misma probabilidad de
ser seleccionados dentro de un rango específico. La aleatoriedad se logra utilizando algoritmos o procesos que generan 
secuencias de números que aparentemente no siguen un patrón discernible.

En la práctica, los números aleatorios se generan utilizando algoritmos de generación de números pseudoaleatorios en 
la mayoría de las computadoras. Estos algoritmos producen secuencias de números que parecen ser aleatorios, pero en realidad 
son deterministas: si se inicia con la misma semilla (un valor inicial), se generará la misma secuencia de números.

Los lenguajes de programación suelen ofrecer funciones o librerías para generar números aleatorios (función random o rand 
o equivalente según el lenguaje de programación). Estos números son utilizados para diversas aplicaciones, como la generación 
de datos para pruebas, simulaciones, criptografía, juegos, entre otros.

El usuario debe intentar adivinar el número (azar) que se generó previamente, y orientar al usuario que tan cerca está de 
ese número hasta que lo encuentre o bien hasta que se le acaben las oportunidades, definir número de oportunidades.


###### Salida: Mensaje de éxito si adivina, mensaje de orientación si no, al agotar las oportunidades mensaje de fracaso.


###### Restricciones: El número n debe estar en el rango de generación de random (En lenguaje C por ejemplo: secreto = rand(100)+1, secreto debiera estar entre 1 y 100).


## DISEÑO 

## En  Lenguaje Natural :

    Se deben declarar variables (secreto, número). 
    
    La variable secreta se debe obtener mediante rand%N o el equivalente según el lenguaje. 
        
    Repetir
        
    Solicitar al participante un número. 
        
    Si adivina se le reporta con el mensaje “felicidades, ¡has adivinado!” y termina,
        
    de lo contario comprobar si este número leído es mayor o menor que el secreto y orientar al usuario, al final se debe reportar 
        
    “Fallo” en caso de no acertar. 
       
    10 intentos o hasta que acierte


## En Diagrama N-S
![](Imagen1.png)


# (C)odificación en C v1
```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int numero,leido;
    srand(time(NULL));
    numero = rand()%100+1;
    do{
        printf("Ingresa un numero");
        scanf("%d",&leido);

        if (numero<leido)printf("El numero a adivinar menor que el ingresaste\n");
        if (numero>leido)printf("El numero a adivinar es mayor que el que ingresaste\n");   
  
    } while (leido!=numero);
    
    printf("Felicidades, has adivinado!! ");

    return EXIT_SUCCESS;
} 
```
# (C)odificación en C v2
```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    int numero,leido,intentos,acierto;
    srand(time(NULL));
    numero = rand()%100 + 1;
    intentos=10;
    acierto=0;

    do{
        do{
            printf("Ingresa un numero\n");
            scanf("%d",&leido);

            if (leido>100 || leido<1)printf("El numero no esta en el rango del juego");

        } while (leido>100 || leido<1);

        if (numero<leido)printf("El numero a adivinar menor que el ingresaste\n");
        if (numero>leido)printf("El numero a adivinar es mayor que el que ingresaste\n"); 
        if (leido==numero) acierto=1;
        intentos--;
        
    } while (acierto==0 && intentos>0); system("cls");

    if(acierto==1)printf("Felicidades, has adivinado en (%d) intentos!!.\nEl numero es el (%d)",10-intentos,numero);
    else printf("Lo siento, has fallado. El numero generado al azar es el (%d)",numero);
    system("pause");

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python
```py
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
```
# (P)ruebas

    |      Entrada                     | Salida                                                |
     (considerando que generado = 55)
    |----------------------------------|-------------------------------------------------------|
    
    | -1                               | El número no está en el rango de juego                |
    
    | 54                               | El número por adivinar es mayor que el que ingresaste |
    
    | 100                              | El número por adivinar es menor que el que ingresaste |
    
    | 55                               | ¡¡Felicidades, has adivinado!!                        |
