#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <math.h>

int main(int argc,char * argv[]){
    int myid,numprocs;
    int buffer;
    MPI_Status status;

    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD,&myid);
    int tag=123;
    int source=0;
    int dest=1;
    int count=1;

    if(myid==source){
        buffer=2015;
        MPI_Send(&buffer,count,MPI_INT,dest,tag,MPI_COMM_WORLD);
        printf("processor %d received %d\n",myid,buffer );
    }
    if(myid ==dest){
        MPI_Recv(&buffer,count,MPI_INT,source,tag,MPI_COMM_WORLD,&status);
        printf("processor %d received %d\n",myid,buffer);
    }
    MPI_Finalize();
    return 0;

}