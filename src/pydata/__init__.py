# read version from installed package
from importlib.metadata import version

__version__ = version("pydata")
from pydata.utils import *
