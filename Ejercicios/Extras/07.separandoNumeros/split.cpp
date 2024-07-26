#include <bits/stdc++.h>
#include <cstdio>
using namespace std;
void funcion();

int main(){

#ifndef texto
    freopen("input.txt", "r", stdin);   // file input.txt is opened in reading mode i.e "r"
    freopen("output.csv", "w", stdout); // file output.txt is opened in writing mode i.e "w"
#endif

    funcion();
    return 0;
    
}


void funcion(){
    int n;
    cin >> n;
    while (n != 0){
        int a = 0, b = 0;
        int la = __builtin_clz(n); // cuenta la cantidad de ceros que tiene algun numero antes del primer uno en binario 
        int k = 1 << n;            // crea bit con una traslacion en un solo espacio
        bool ver = false; //esto es un switch que va cambiando los elementos entre a y b 
        int lar = 32-la;     //saca la diferencia, o sea el tamaño del numero en binario
        for (int i = 0 ; i<lar ; i++){ 
            if ((n & (1 << i)) != 0){
                if (!ver){
                    a += (n & (1 << i));
                }
                else{
                    b += (n & (1 << i)); // crea un and logico entre 2 bits
                }
                ver = !ver;
            }
        }
        cout << a << ", " << b << "\n";
        cin >> n;
    }
}