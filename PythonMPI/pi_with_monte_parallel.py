from mpi4py import MPI 
import time 
import random
from numba import jit

max_iteration=100000000
@jit
def calc_pi_single(iteration):
    counter=0
    for _ in range(iteration):
        x=random.random()
        y=random.random()
        if x**2+y**2<1:
            counter+=1
    return 4.0*counter/iteration

def divide_task(task,nprocs):
    divided_size=len(task)//nprocs
    divided=[]
    residue=[]
    for i in range(0,len(task),divided_size):
        if i+divided_size<=len(task):
            task_divided=task[i:i+divided_size]
            divided.append(task_divided)
        else:
            residue=task[i:]
    divided[0]+=residue
    return divided

def main():
    master=0
    comm=MPI.COMM_WORLD
    nprocs=comm.Get_size()
    myrank=comm.Get_rank()
    args=None
    iteration=0
    if myrank==master:
        start=time.time()
        iteration=max_iteration//nprocs
        args=[ iteration  for _ in range(nprocs)]
    iteration=comm.scatter(args,root=master)
    pi_each_rank=calc_pi_single(iteration)
    results=comm.gather(pi_each_rank,root=master)
    if myrank==master:
        avg=sum(results)/float(nprocs)
        print("approx pi=",avg,"elapsed time=",time.time()-start)

if __name__ == '__main__':
    main()