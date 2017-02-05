from mpi4py import MPI 

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
sendmsg=rank

print("I am rank {} I have sendmsg as {}".format(rank,sendmsg))
recvmsg1=comm.reduce(sendmsg,op=MPI.SUM,root=0)

if rank==0:
    print("rank zero",recvmsg1)

print("all reduce at rank {}".format(rank))
recvmsg2=comm.allreduce(sendmsg,op=MPI.SUM)
print("I am rank {} I have recvmsg2 op=MPI.SUM as {}".format(rank,recvmsg2))