

import click

from datetime import datetime as dt
from multiprocessing import Pool, cpu_count

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


def count_tokens(path):

    """
    Count tokens in a volume.

    Args:
        path (str)
    """

    try:

        vol = Volume.from_bz2_path(path)
        return vol.token_count()

    except Exception as e:
        print(e)


@click.command()
@click.argument('seconds', default=3600)
def parallel(seconds):

    """
    Parallelize across N cores.
    """

    print(cpu_count())

    corpus = Corpus.from_env()

    v = 0
    t = 0

    t1 = dt.now()

    with Pool() as pool:

        jobs = pool.imap_unordered(
            count_tokens,
            corpus.paths('.bz2'),
        )

        for count in jobs:

            if count: t += count
            v += 1

            # Break after N seconds.
            if (dt.now()-t1).total_seconds() > seconds:
                print(v, t)
                break


if __name__ == '__main__':
    parallel()
