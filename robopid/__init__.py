
"""
robo-pid - PID Controller for Mobile Robotics
"""

# flit uses __version__ as one source version 
# setup.cfg uses version = attr: robopid.__version__ 
# note: pypi pep versions like this form > 'x.y.<number>[a-c]<digit>'
# but 0.01.08d doesnt fly building from pyproject.toml


__version__ = 'v0.02.06a'

# import acts to export 

from .pid import RoboPid
from .pid import RoboPid as Pid
from .pid import RoboPid as RoboPID



