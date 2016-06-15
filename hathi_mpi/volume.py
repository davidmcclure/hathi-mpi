

import json
import bz2


class Volume:


    @classmethod
    def from_path(cls, path):

        """
        Inflate a volume and make an instance.

        Args:
            path (str)

        Returns: cls
        """

        with bz2.open(path, 'rt') as fh:
            return cls(json.loads(fh.read()))


    def __init__(self, data):

        """
        Read the compressed volume archive.

        Args:
            data (dict)
        """

        self.data = data


    @property
    def id(self):

        """
        Get the HTRC id.

        Returns: str
        """

        return self.data['id']
