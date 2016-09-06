from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

for i in range(size):
    txtname='t'+str(i)+'.txt'
    if rank==i:
        with open(txtname,'w') as f:
            print("myrank is {}".format(rank))
            f.write("rank {} wrote".format(rank))