#include <stdio.h>

float f(float x);
int main(){
    float integral;
    float a,b;
    int n;
    float h;
    float x;
    float i;
    printf("Enter a,b and n\n");
    scanf("%f %f %d",&a,&b,&n);

    h=(b-a)/n;
    integral=(f(a)+f(b))/2.0;
    x=a;
    for(int i=1;i<n;i++){
        x+=h;
        integral+=f(x);
    }
    integral*=h;

    printf("with n = %d trapezoids, our estimate\n",n );
    printf("of the intefral from %f to %f = %f\n",a,b,integral );    
}

float f(float x){
    float val;
    val=x*x;
    return val;
}