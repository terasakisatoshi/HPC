#include <stdio.h>
#include <stdlib.h>
#include <time.h>
double myrand(void){
    return (double)rand()/(double)RAND_MAX;
}

double calc_pi(int seed,int trial){
    srand(time(NULL));
    int n=0;
    for (int i = 0; i < trial; ++i)
    {
        double x=myrand();
        double y=myrand();
        if(x*x+y*y<1.0){
            n++;
        }
    }
    return 4.0*(double)n/(double)trial;
}

int main(){
    double pi=calc_pi(1,100000000);
    printf("pi=%f\n",pi );
}