#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int main(int argc, char* argv[]) {
	int myid, numprocs;
	int tag, source, dest, count;
	int buffer;
	MPI_Status status;
	MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &myid);
	tag = 123;
	count = 1;
	source = 0;
	dest = 1;

	MPI_Request request;
	request = MPI_REQUEST_NULL;
	if (myid == source) {
		buffer = 2015;
		MPI_Isend(&buffer, count, MPI_INT, dest, tag, MPI_COMM_WORLD, &request);
	}
	if (myid == dest) {
		MPI_Irecv(&buffer, count, MPI_INT, dest, tag, MPI_COMM_WORLD, &request);

	}

	MPI_Wait(&request, &status);
	if (myid == source) {
		printf("processor %d sent %d\n", myid, buffer);
	}
	if (myid == dest) {
		printf("processor %d received %d\n", myid, buffer);
	}
	MPI_Finalize();
	return 0;

}