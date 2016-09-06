#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

double myrand(void){
    return (double)rand()/(double)RAND_MAX;
}

double calc_pi(int seed,int trial){
    srand(seed);
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

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    int rank,size;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    double pi=calc_pi(rank,10000000);
    printf("pi=%f\n",pi );
    MPI_Finalize();
    return 0;
}