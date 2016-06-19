

from mpi4py import MPI

from hathi_mpi import config
from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume
from hathi_mpi.utils import enum


Tags = enum('READY', 'WORK', 'EXIT')


def loops():

    """
    Generate and processs the paths in parallel - break of N paths, send to
    worker, break off another N paths, etc.
    """

    comm = MPI.COMM_WORLD

    size = comm.Get_size()
    rank = comm.Get_rank()

    status = MPI.Status()

    if rank == 0:

        corpus = Corpus.from_env()

        path_groups = corpus.path_groups('.bz2', config['group_size'])

        count = 0

        closed_ranks = 0

        while closed_ranks < size-1:

            # Get a work request from a rank.
            data = comm.recv(
                status=status,
                source=MPI.ANY_SOURCE,
                tag=MPI.ANY_TAG,
            )

            source = status.Get_source()
            tag = status.Get_tag()

            # -----
            # READY
            # -----
            if tag == Tags.READY:

                # Try to send a new group of paths.
                try:
                    paths = next(path_groups)
                    comm.send(list(paths), dest=source, tag=Tags.WORK)
                    print(rank, 'work', source)

                # If finished, close the rank.
                except StopIteration:
                    comm.send(None, dest=source, tag=Tags.EXIT)
                    print(rank, 'exit', source)

            # ----
            # EXIT
            # ----
            elif tag == Tags.EXIT:
                count += data
                closed_ranks += 1

        print(count)

    else:

        count = 0

        while True:

            # Ready for work.
            comm.send(None, dest=0, tag=Tags.READY)

            # Request paths.
            paths = comm.recv(
                source=0,
                tag=MPI.ANY_TAG,
                status=status,
            )

            tag = status.Get_tag()

            # ----
            # WORK
            # ----
            if tag == Tags.WORK:

                # Count tokens in segment.
                for path in paths:

                    try:

                        vol = Volume.from_bz2_path(path)
                        count += vol.token_count()

                    except Exception as e:
                        print(e)

            # ----
            # EXIT
            # ----
            elif tag == Tags.EXIT:
                break

        # Notify exit.
        comm.send(count, dest=0, tag=Tags.EXIT)


if __name__ == '__main__':
    loops()
