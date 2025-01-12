'''
DatasetBundle is a Bundle type that simply inherits from UploadedBundle.
'''
from typing import List

from codalab.objects.bundle import Bundle


class PrivateBundle(Bundle):
    """
    Dummy placeholder subclass of Bundle that is used to mask private bundles.
    """

    BUNDLE_TYPE = 'private'
    METADATA_SPECS = []  # type: List

    @classmethod
    def construct(cls, uuid):
        return cls(
            {
                'uuid': uuid,
                'bundle_type': cls.BUNDLE_TYPE,
                'owner_id': None,
                'command': None,
                'data_hash': None,
                'state': None,
                'frozen': None,
                'is_anonymous': None,
                'dependencies': [],
                'metadata': {'name': '<private>'},
            }
        )
