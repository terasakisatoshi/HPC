#include <stdio.h>

int calc_fib(int n){
    double a=0.0, b=1.0, c;
    for(int i=0;i<n;i++){
        c=a+b;
        a=b;
        b=c;
    }
   return a;
}

int main(){
    int n;
    printf("input n s.t. fin(n)\n");
    scanf("%d",&n);
    double a=calc_fib(n);
    printf("%f\n",a);
}