#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

//Blocking Communication

int main(int argc, char* argv[]) {
	int myid;
	int numproces;
	int tag, source, destination, count;
	int buffer;
	MPI_Status status;
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &numproces);
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);
	tag = 123;
	source = 0;
	destination = 1;
	count = 1;
	if (myid == source) {
		buffer = 2015;
		MPI_Send(&buffer, count, MPI_INT, destination, tag, MPI_COMM_WORLD);
		printf("processor %d sent %d \n", myid, buffer);
	}
	if (myid == destination) {
		MPI_Recv(&buffer, count, MPI_INT, destination, tag, MPI_COMM_WORLD,&status);
		printf("processor %d received %d \n", myid, buffer);
	}
	MPI_Finalize();
	return 0;
}