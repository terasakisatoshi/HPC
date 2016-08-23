from mpi4py import MPI
import sys

def f(x):
  return 4 / ( 1.0 + x**2 )

comm = MPI.Comm.Accept()
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

print "starting task-%d on %s " % (rank, name)
print "pi-cluser mas"
N = None
N = comm.bcast(N, root=0)
step = 1.0 / N

start = rank
end = N
skip = size

sum = 0.0
cn = 0
for i in range(start, end, skip):
  x = (i + 0.5) * step
  sum += f(x)
  cn += 1

cpi = sum * step
print "c-pi (task %d on %s,n=%d): %f" % (rank, name, cn, cpi)
comm.reduce(cpi, None, op=MPI.SUM, root=0)

comm.Disconnect()