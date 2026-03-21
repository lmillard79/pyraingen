# read version from installed package
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyraingen")
except PackageNotFoundError:
    __version__ = "unknown"