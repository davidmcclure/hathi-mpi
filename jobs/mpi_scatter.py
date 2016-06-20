

import math

from mpi4py import MPI


comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0:
    data = [4, 9, 16, 25]

else:
    data = None

val = comm.scatter(data, root=0)

results = comm.gather(math.sqrt(val), root=0)

print(results)
