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
		if(x*x+y*y<1){
			n++;
		}
	}
	return 4.0*(double)n/(double)trial;
}

int main(int argc,char ** argv){
	int trial=10000000;
	MPI_Init(&argc,&argv);
	int rank,procs;
	MPI_Comm_size(MPI_COMM_WORLD,&procs);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	double pi=calc_pi(rank,trial);
	printf("myrank is %d of procs %d mypi is %f\n",rank,procs,pi);
	MPI_Barrier(MPI_COMM_WORLD);
	double sum=0;
	MPI_Allreduce(&pi,&sum,1,MPI_DOUBLE,MPI_SUM,MPI_COMM_WORLD);
	sum=sum/double(procs);
	if(0==rank){
		printf("average=%f\n", sum);
	}
	MPI_Finalize();
	return 0;
}