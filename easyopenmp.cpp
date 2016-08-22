#include <stdio.h>
int main(int argc, char const *argv[])
{
    int a=0;
    #pragma omp parallel for reduction(+:a)
    for(int i=0;i<100000;i++){
        for (int j = 0; j < 100000; ++j)
        {
            a++;
            a=a%3;
        }
    }
    printf("%d",a);
    return 0;
}