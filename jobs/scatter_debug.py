

import json
import numpy as np
import math

from mpi4py import MPI


def scatter():

    """
    Walk all paths, scatter to workers, rather sub-sums.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # Split paths into segments.

    if rank == 0:

        paths = ['/scratch/PI/malgeeh/htrc/hvd/pairtree_root/ar/k+/=1/39/60/=t/00/02/fm/9b/ark+=13960=t0002fm9b/bc.ark+=13960=t0002fm9b.basic.json.bz2'] * 5000000

        splits = np.array_split(paths, size)

        segments = [json.dumps(list(s)) for s in splits]

    else:
        segments = None

    # Count tokens in segment.

    segment = comm.scatter(segments, root=0)

    count = 0

    for path in json.loads(segment):
        count += 1

    # Merge segment sub-totals.

    counts = comm.gather(count, root=0)

    if rank == 0:
        print(sum(counts))


if __name__ == '__main__':
    scatter()
