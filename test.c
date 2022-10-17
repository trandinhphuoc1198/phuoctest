#include<stdio.h>
void cl(int*  a){

    printf("%d\n",&a);
    
}

int main(){
    int player[2][2] = {{1,2}};
    
    printf("%d\n",*player);
    printf("%d\n",&player[0]);
    printf("%d",player[0][2]);


    return 0;
}