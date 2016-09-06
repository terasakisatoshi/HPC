#include <stdio.h>
#include <mpi.h>

struct Parameter{
    int seed;
    double temperature;
};

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    int rank=0;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    Parameter param;
    if(0==rank){
        printf("scan param.seed\n");
        scanf("%d",&param.seed);
        printf("scan param.temperature\n");
        scanf("%lf",&param.temperature);
    }
    int root=0;//master
    MPI_Bcast(&param,sizeof(param),MPI_BYTE,root,MPI_COMM_WORLD);
    printf("rank=%d:seed=%d temperature=%f\n",rank,param.seed,param.temperature );
    MPI_Finalize();
    return 0;
}