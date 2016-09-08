import os
from os.path import join
from glob import glob
from mpi4py import MPI 
import subprocess

comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size

if rank==0:
    template=join(os.getcwd(),'t*.txt')
    files=glob(template)
    partitions=[[] for i in range(size)]
    for i,file in enumerate(files):
        partitions[i%size].append(file)
    #print('partitions=%s\n'%partitions)

    for i in range(1,len(partitions)):
        comm.send(partitions[i],dest=i,tag=i)
    filelist=partitions[0]

if rank!=0:
    filelist=comm.recv(source=0,tag=rank)

print('I am rank {} of size {}'.format(rank,size))
print(filelist)
comm.Barrier()
for file in filelist:
    command="hello.exe"+" "+str(file)
    echo="echo "+command
    subprocess.call(echo,shell=True)
    subprocess.call(command,shell=True)
comm.Barrier()
print('finish rank %s'%rank)

