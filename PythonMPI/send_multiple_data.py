#note that this program is expected max procces rank is 2
#otherwize rank which is more than 2 cannot receive and wait forever.
#It means master cannot finish calulation. 
#So please be careful.
from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size
name=MPI.Get_processor_name()
if rank==0:
    print("Hi I'm master")
    message1={'d1':55,'d2':42}
    comm.send(message1,dest=1,tag=1)
    message2={'d3':25,'d4':22}
    comm.send(message2,dest=1,tag=2)
else:
    print("Greetings my master, this is %s"% name)
    receive2=comm.recv(source=0,tag=2)
    print receive2
    receive1=comm.recv(source=0,tag=1)
    print receive1
