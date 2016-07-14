

import os
import numpy as np
import json

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

    def json_segments(self, size=256):

        """
        Split the paths into a list of JSON-encoded segments.

        Args:
            size (int)
        """

        return [
            json.dumps(list(s))
            for s in np.array_split(self.paths, size)
        ]
