

import math

from mpi4py import MPI


comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0:
    comm.send(4, dest=1)
    comm.send(9, dest=2)
    comm.send(16, dest=3)

if rank == 1:
    val = comm.recv(source=0)
    print('rank 1', math.sqrt(val))

if rank == 2:
    val = comm.recv(source=0)
    print('rank 2', math.sqrt(val))

if rank == 3:
    val = comm.recv(source=0)
    print('rank 3', math.sqrt(val))
