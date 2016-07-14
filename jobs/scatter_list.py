

import numpy as np
import json

from datetime import datetime as dt
from mpi4py import MPI

from hathi_mpi.manifest import Manifest
from hathi_mpi.volume import Volume


def scatter():

    """
    Walk all paths, scatter to workers, rather sub-sums.
    """

    t1 = dt.now()

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    # Get JSON-encoded segments.

    if rank == 0:

        manifest = Manifest.from_env()

        segments = manifest.json_segments(size)

        # Duration.
        t2 = dt.now()
        print((t2-t1).total_seconds())

    else:
        segments = None

    # Count tokens in segment.

    segment = comm.scatter(segments, root=0)

    count = 0

    for i, path in enumerate(json.loads(segment)):

        try:

            vol = Volume.from_bz2_path(path)
            count += vol.token_count()

        except Exception as e:
            print(e)

        if i%1000 == 0:
            print(rank, i)

    # Merge segment sub-totals.

    counts = comm.gather(count, root=0)

    if rank == 0:

        # Duration.
        t3 = dt.now()
        print((t3-t1).total_seconds())

        # Total count.
        print(sum(counts))


if __name__ == '__main__':
    scatter()
