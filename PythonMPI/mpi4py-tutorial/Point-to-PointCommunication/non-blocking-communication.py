from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.Get_rank()

if rank==0:
    data={"a": 7,"b":4}
    req=comm.isend(data,dest=1,tag=11)
    req.wait()
elif rank==1:
    req=comm.irecv(source=0,tag=11)
    data=req.wait()
    print("rank 1 got data from zero\n")
    print("its data is {}".format(data))
