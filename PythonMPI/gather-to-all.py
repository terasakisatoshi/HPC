from mpi4py import MPI 
comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

sendmsg=rank**2
print("Hello! I am rank {} I have msg {}".format(rank,sendmsg))
gathermsg=comm.gather(sendmsg,root=0)
allgathermsg=comm.allgather(sendmsg)
if rank ==0:
    print("I am rank {} I gather msg {}".format(rank,gathermsg))

print("I am rank {} I got allgather data =\n {}".format(rank,allgathermsg))
