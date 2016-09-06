#include <iostream>
#include <fstream>
#include <mpi.h>
using namespace std;
int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    int rank,procs;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&procs);
    const int SIZE=2;
    int array[SIZE];
    for (int i = 0; i < SIZE; ++i)
    {
        array[i]=rank;
    }

    if(0==rank){
        ofstream ofs("data.dat");
        ofs.close();
    }
    for (int j = 0; j < procs; ++j)
    {
        MPI_Barrier(MPI_COMM_WORLD);
        if(j!=rank){
            continue;
        }
        std::ofstream ofs("data.dat",std::ios::app);
        for (int i = 0; i < SIZE; ++i)
        {
            ofs<<array[i]<<endl;
        }
        ofs.close();
    }
    MPI_Finalize();
}