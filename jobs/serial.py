

import click

from datetime import datetime as dt

from hathi_mpi.manifest import Manifest
from hathi_mpi.volume import Volume


@click.command()
@click.argument('seconds', default=3600)
def serial(seconds):

    """
    Loop through volmes one-by-one.
    """

    manifest = Manifest.from_env()

    v = 0
    t = 0

    t1 = dt.now()

    for path in manifest.paths:

        try:

            vol = Volume.from_bz2_path(path)
            t += vol.token_count()
            v += 1

        except Exception as e:
            print(e)

        # Break after N seconds.
        if (dt.now()-t1).total_seconds() > seconds:
            print(v, t)
            break


if __name__ == '__main__':
    serial()
