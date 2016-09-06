#include <stdio.h>
#include <mpi.h>

int main(int argc,char **argv){
	MPI_Init(&argc,&argv);
	int rank=0;
	int nprocs;
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&nprocs);
	int value=0;
	if(0==rank){
		printf("input int value\n");
		scanf("%d",&value);
	}
	MPI_Bcast(&value,1,MPI_INT,0,MPI_COMM_WORLD);
	printf("rank=%d: value%d\n", rank,value);
	MPI_Finalize();
	return 0;
}