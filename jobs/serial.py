

import click

from datetime import datetime as dt

from hathi_mpi.corpus import Corpus
from hathi_mpi.volume import Volume


@click.command()
@click.argument('seconds', default=3600)
def serial(seconds):

    """
    Loop through volmes one-by-one.
    """

    corpus = Corpus.from_env()

    v = 0
    t = 0

    t1 = dt.now()

    for path in corpus.paths('.bz2'):

        try:

            vol = Volume.from_bz2_path(path)
            t += vol.token_count()
            v += 1

        except Exception as e:
            print(e)

        if (dt.now()-t1).total_seconds() > seconds:
            print(v, t)
            break


if __name__ == '__main__':
    serial()
