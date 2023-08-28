
"""
basic-pid - PID Controller for discretized time
"""

# flit uses __version__ as one source version 
# note: pep versions like > 'x.y.<number>[a-c]<digit>'
# for example: 0.01.08d doesnt fly building from pyproject.toml

__version__ = 'v0.02.01'

# import acts to export 

from .pid import BasicPid
from .pid import BasicPid as Pid


