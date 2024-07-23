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
// Me genera con error el caso de .i... ya que genera "Cindysalio mal"