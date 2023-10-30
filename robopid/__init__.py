
"""
robo-pid - PID Controller Mobile Robotics
"""

# flit uses __version__ as one source version 
# note: pep versions like > 'x.y.<number>[a-c]<digit>'
# for example: 0.01.08d doesnt fly building from pyproject.toml

__version__ = 'v0.02.05'

# import acts to export 

from .pid import RoboPid
from .pid import RoboPid as Pid


