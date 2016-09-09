from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
name = MPI.Get_processor_name()
if rank==0:
    data=[(i+1)**2 for i in range(size)]
    print("rank {} make data = {}".format(rank,data))
else:
    data=None
    print("I am rank {} of size {} on {}".format(rank,size,name))
data=comm.scatter(data,root=0)
print("rank {} has data {}".format(rank,data))
assert data== (rank+1)**2