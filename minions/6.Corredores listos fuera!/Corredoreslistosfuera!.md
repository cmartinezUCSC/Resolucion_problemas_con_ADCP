# 6.Corredores listos fuera!  
#### Dificultad: fácil

## Descripcion

*Los corredores del Ironman de Pucón, una bella ciudad al sur de Chile, requieren determinar la velocidad (m/s) promedio por competidor alcanzada en una de las rutas de 1500 metros. El registro incluye parejas de números (minutos: segundos) por cada corredor correspondiente al tiempo exacto que les tomó la ruta. El término de la lista de corredores está determinado porque la dupla minutos: segundos es 0:0.*


# Solución ADCP

# (A)NÁLISIS
###### Entradas:Tiempo (minutos, segundos) que le toma a cada corredor completar la ruta.   

###### Proceso mental: ¿Debería hacer la transformación de minutos a segundos? ¿Cómo lo hago? ¿Cómo obtener la velocidad?  ¿Debería saber cuántos corredores participaron en la ruta? 
*Imaginemos un ejemplo en las entradas: (tiempo que se demoraron en completar los 1500 metros un grupo de 4 participantes)*

        |      Minutos:Segundos | Velocidad (m/s)          |
        |-----------------------|--------------------------|
        
        | 2:30                  | 1500(m)/150(s)=10 m/s    |
        
        | 3:00                  | 1500(m)/180(s)=8.33 m/s  |
        
        | 1:58                  | 1500(m)/118(s)=12.71 m/s |

        | 3:01                  | 1500(m)/181(s)=8.28 m/s  |




## DISEÑO 

## En  Lenguaje Natural :

    1.	Definir las variables minuto, segundo, promedio y velocidad. 
    2.	Leer variables minuto y segundo hasta ingresar un par 0 0. 
    3.	Se valida que los tiempos sean válidos (minuto, segundo ≥0). 
    4.	Si ingreso una pareja válida, se debe obtener su equivalente en segundos (tiempo=segundos+60*minutos). 
    5.	Obtenido el tiempo en segundos, calcular velocidad (longitud/tiempo(s)) y mostrar en pantalla.


## En Diagrama N-S


# (C)odificación en C
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int minutos,segundos,tiempo;
    float velocidad;

    do{
        do
        {
            printf("Ingrese tiempos en mm ss: ");
            scanf("%d %d",&minutos,&segundos);
            if(minutos<0 || segundos<0) printf("\nha ingresado un valor invalido, debe ser >=0. Reintente!\n ");
        } while (minutos<0 || segundos<0);
        
        if (segundos!=0 || minutos!=0){
            tiempo=segundos+(minutos*60);
            velocidad=1500/(float)tiempo;
            printf("La velocidad promedio es de: %.2f m/s\n",velocidad);
        }    
        
    } while (minutos!=0 || segundos!=0);   

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python
```py
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
```
# (P)ruebas

        
        |Entrada (Minutos:Segundos) | Salida                            |
        |-------------------------- |-----------------------------------|
        
        | 2:30                      | 1500(m)/150(s)=10.00 m/s          |
        
        | 4:00                      | La velocidad promedio es 6.25 m/s |
        
        |-3:00                      | Entrada errónea. ¡Reintente!      |
        
        | 0:0                       | cierre programa                   |

