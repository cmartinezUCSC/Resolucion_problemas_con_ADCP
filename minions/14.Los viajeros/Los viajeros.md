# 14.Los viajeros

#### Dificultad: fácil

## Descripcion

Alice, Bob y Cindy han decidido irse de viaje por las fiestas! Mientras el resto de sus amigos han ido a vacacionar a Japón y Europa, estos tres amigos han decidido una alternativa más divertida (y económica), explorar las filipinas en grupo. Por pura coincidencia los 3 compraron la misma maleta para llevarla al viaje. Por buena suerte todos decidieron rotular sus maletas con su nombre (estas etiquetas distinguen entre mayúsculas y minúsculas). Por desgracia en estas etiquetas se han ido borrando algunas letras con el tiempo, al menos tienes asegurado que el largo de la palabra se mantiene, Ayudémosles a que pasen unas vacaciones libres de estrés escribiendo un programa que identifique al dueño de la maleta una etiqueta poco legible asumiendo que el dueño es Alice, Bob o Cindy.


| Entrada | Salida             |
|---------|--------------------|
| Ali.e   | Alice              |
| bob     | SOMETHING'S WRONG  |
| .i...   | Cindy              |

# ADCP

## (A)nalisis

###### Entradas: 
Un string S conteniendo caracteres alfabéticos y/o punto (.)


###### Proceso:

Lo primero que podemos filtrar, es el caso de que el nombre ingresado devuelva "SOMETHING'S WRONG", eso en primer momento lo podemos solucionar de forma muy sencilla con una pregunta, ¿el string que nos entregan tiene 3 ó 5 caracteres? si la respuesta es no, imprimimos "SOMETHING'S WRONG" y terminaríamos el ejercicio, si la respuesta en un si por otro lado, podríamos ver como progresa, primero viendo con el caso de que fuera de solo 3 caracteres de largo.

Evaluaremos los distintos casos que se pueden dar, para ello usamos a Bob, como Bob solo tiene 3 caracteres podríamos comparar los posibles casos y compararlos uno a uno.

| B  | .        | .        |
|----|----------|----------|
| B  | o        | b        |
| si | puede ser| puede ser|

*En este caso como la cantidad de caracteres es 3 y el único caracter que nos da la pista es correcto, podemos asumir que es la maleta de bob.*

| b  | o   | b   |
|----|-----|-----|
| B  | o   | b   |
| NO | si  | si  |

*En este caso la maleta no es de bob porque el escribe su nombre con una mayúscula al principio por lo que imprimiríamos SOMETHING'S WRONG.*

| .       | .      | .       |
|---------|--------|---------|
| B       | o      | b       |
| tal vez | tal vez| tal vez |

*En este caso la respuesta sería Bob puesto que es la única posibilidad con tres caracteres de los tres nombres, ahora bien, en caso de que el largo sea de 5 tenemos un poco más de variedad, para eliminar la posibilidad de que sea cualquiera, se descarta la posibilidad de que sea cualquiera de los 2 nombres por lo que, si diera que entregan, se sabrá al instante que se debe imprimir CAN'T TELL*

*Si ese no fuera el caso habría que ver como reconocer a que persona corresponde, para eso podríamos ir comparando letra a letra de nuevo, pero ahora viendo que palabra forma de forma que si es un punto asumimos que es la letra correcta y si en algún momento aparece una letra que no calza intentamos con la otra persona posible.*


###### Salida: 

Se asume el dueño de la maleta que puede ser Alice, Cindy o Bob entonces para la salida tenemos 3 opciones posibles,
•	Si con las letras visibles solo puede ser uno de los 3 nombres entonces se imprime el nombre.
•	Si existiera más de una posibilidad se imprime CAN'T TELL
•	Si el nombre no coincide con ninguno de los 3 se imprime SOMETHING'S WRONG
 

###### Restricciones: 

S debe tener entre 1 a 5 caracteres, estos caracteres deben ser caracteres alfabéticos en mayúsculas o minúsculas o puede ser un punto

# (D)iseño

## En Diagrama N-S

![](Imagen.png)

# (C)odificación en C
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char S[10];
    scanf("%s", S);

    char* nom[3] = {"Bob", "Alice", "Cindy"};
    char resp[10] = "";

    if (strlen(S) == 3){
        for (int i = 0; i < 3; i++){
            if (S[i] == nom[0][i]){
                resp[i] = S[i];
            }else if (S[i] == '.'){
                resp[i] = nom[0][i];
            }else{
                strcpy(resp, "algo salio mal");
                break;
            }  
        }  
    }else if (strcmp(S, ".....") == 0){
        strcpy(resp, "NO SE PUEDE DETERMINAR");
    }else{
        for (int i = 0; i < 5; i++){
            if (S[i] == nom[1][i]){
                resp[i] = S[i];
            }else if (S[i] == '.'){
                resp[i] = nom[1][i];
            }else{
                strcpy(resp, "algo salio mal");
                break;
            }
        }
        resp[5] = '\0';
        if (strcmp(resp, nom[1]) != 0){
            strcpy(resp, "");
            for (int i = 0; i < 5; i++){
                if (S[i] == nom[2][i]){
                    resp[i] = S[i];
                }else if (S[i] == '.'){
                    resp[i] = nom[2][i];
                }else{
                    strcpy(resp, "algo salio mal");
                    break;
                }
            }   
        }
    }
    
    printf("%s\n", resp);

    return EXIT_SUCCESS;
}
```
# (C)odificación en Python
```py
S = input()

nom = ["Bob", "Alice", "Cindy"]

resp = ""

if len(S) == 3:
    for i in range(3):
        if S[i] == nom[0][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[0][i]
        else:
            resp = "algo salio mal"
            break

elif S == ".....":
    resp = "NO SE PUEDE DETERMINAR"
else:
    for i in range(5):
        if S[i] == nom[1][i]:
            resp = resp + S[i]
        elif S[i] == ".":
            resp = resp + nom[1][i]
        else:
            resp = "algo salio mal"
            break
    
    if resp != nom[1]:
        resp = ""
        
        for i in range(5):
            if S[i] == nom[2][i]:
                resp = resp + S[i]
            elif S[i] == ".":
                resp = resp + nom[2][i]
            else:
                resp = "algo salio mal"
                break

print(resp)
```
# (P)ruebas

      | Entrada  | Salida             |
      
      |----------|--------------------|
      
      | Ali.e    | Alice              |
      
      | bob      | algo salio mal     |
      
      | .i...    | Cindy              |