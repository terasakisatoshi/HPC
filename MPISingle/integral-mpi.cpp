#include <stdio.h>
#include <mpi.h>

float Trap(float local_a,float local_b,int local_n,float h);  
float f(float x);

int main(int argc, char *argv[])
{
    int myrank;
    int nproc;
    float a=0.0;
    float b=1.0;
    int n=100000;
    float h;
    
    float local_a;
    float local_b;
    int local_n;

    float integral;
    double total;
    int dest_master=0;
    int tag=0;

    MPI_Status status;
    //start MPI
    MPI_Init(&argc, &argv);
    //get current process
    MPI_Comm_rank(MPI_COMM_WORLD,&myrank);
    //get num of process
    MPI_Comm_size(MPI_COMM_WORLD,&nproc);

    h=(b-a)/n;
    local_n=n/nproc;
    local_a=a+myrank*local_n*h;
    local_b=local_a+local_n*h;
    integral=Trap(local_a,local_b,local_n,h);

    if(myrank==0){//master
        total=integral;
        for(int source=1;source<nproc;source++){
            MPI_Recv(&integral,1,MPI_FLOAT,source,tag,MPI_COMM_WORLD,&status);
            total+=integral;
        }
    }else{//slave
        MPI_Send(&integral,1,MPI_FLOAT,dest_master,tag,MPI_COMM_WORLD);
    }

    //print output
    if(myrank==0){
        printf("With n = %d trapezoids, out estimate\n", n);
        printf("of the integral from a to %f = %f \n",b,total);
    }
    //end MPI
    MPI_Finalize();
    return 0;
}

float Trap(float local_a,float local_b,int local_n,float h){
    float x=local_a;
    float integral=(f(local_a)+f(local_b))/2.0;
    for(int i=1;i<local_n;i++){
    x+=h;
    integral+=f(x);
    }
    integral*=h;
    return integral;
}

float f(float x){
    float val=x*x;
    return val;
}