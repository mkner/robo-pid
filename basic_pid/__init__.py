
"""
basic-pid - PID Controller for discretized time
"""

# flit uses this as one source version #
# note: pep whatever doesnt like > 'x.y.<number>c'
# for example: 0.01.08d doesnt fly building from pyproject.toml

__version__ = '0.01.10b'

# import acts to export 

from .pid import BasicPid
from .pid import BasicPid as Pid


