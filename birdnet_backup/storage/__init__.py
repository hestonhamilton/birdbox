# storage/__init__.py

from .storage_interface import StorageInterface
from .local_storage import LocalStorage
from .network_storage import NetworkStorage
from .cloud_storage import CloudStorage

# __all__ is an optional list of module names or other objects that should be imported when from <package> import * is encountered.
__all__ = ['StorageInterface', 'LocalStorage', 'NetworkStorage', 'CloudStorage']
