

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

    vol_count = 4801237
    scatter_count = math.floor(vol_count/size)*size

    # Split paths into segments.

    if rank == 0:

        paths = (['data/pairtree_root/ar/k+/=1/39/60/=t/00/02/fm/9b/ark+=13960=t0002fm9b/bc.ark+=13960=t0002fm9b.basic.json.bz2'] * 4801237)[:scatter_count]

        segments = np.array(np.split(np.array(paths), size))

    else:
        segments = None

    # Count tokens in segment.

    segment = np.empty(int(scatter_count/size), dtype='<U200')

    comm.Scatter([segments, MPI.CHAR], [segment, MPI.CHAR])

    count = 0

    for path in segment:
        count += 1

    # Merge segment sub-totals.

    counts = comm.gather(count, root=0)

    if rank == 0:
        print(sum(counts))


if __name__ == '__main__':
    scatter()
