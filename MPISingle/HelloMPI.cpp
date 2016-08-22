#include <stdio.h>
#include <string.h>
#include <mpi.h>

int main(int argc,char * argv[]){
    int myrank;
    int nproc;
    int dest;
    int tag=0;
    //allocate message
    char message[100];
    //受信戻りのステータス
    MPI_Status status;
    MPI_Init(&argc,&argv);
    //get current process rank
    MPI_Comm_rank(MPI_COMM_WORLD,&myrank);
    //get num of process 
    MPI_Comm_size(MPI_COMM_WORLD,&nproc);
    if(myrank!=0){
        sprintf(message,"Greetings from process(i.e. rank) %d!",myrank);
        dest=0;
        MPI_Send(message,strlen(message)+1,MPI_CHAR,dest,tag,MPI_COMM_WORLD);
    }else{// myrank==0 i.e. master
        for(int source =1 ;source<nproc;source++){

        MPI_Recv(message,100,MPI_CHAR,source,tag,MPI_COMM_WORLD,&status);
        printf("%s\n", message);
        }
    }

    MPI_Finalize();
    return 0;
}