

import os

from hathi_mpi import config


class Manifest:

    @classmethod
    def from_env(cls):

        """
        Wrap the ENV-defined manifest.

        Returns: cls
        """

        return cls(
            config['corpus']['features'],
            config['corpus']['manifest'],
        )

    def __init__(self, features_path, manifest_path):

        """
        Read and normalize the paths.

        Args:
            features_path (str)
            manifest_path (str)
        """

        with open(manifest_path, 'r') as fh:

            self.paths = [
                os.path.join(features_path, path)
                for path in fh.read().splitlines()
            ]
