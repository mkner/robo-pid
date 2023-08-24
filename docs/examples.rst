

Example
-------

basic-pid
*************

For example:

>>> import basic_pid

>>> p = basic_pid.BasicPid()

Or just:

>>> from basic_pid import Pid

>>> p = Pid()

>>> p.name()
'BasicPid'

>>> p.vers()
'v0.01.10a'

>>> p.desc()
'Basic Discrete Time PID Controller'






roboclocks
**********

Included here as another example. Not installed with **new-pyproject**

To use this project, first install it using pip:

.. code-block:: console

    $ pip install roboclocks



To get current time and date info based on the current underlying 
system OS/HW configuration for place/timezone you can use several 
functions 


For basic numeric date/time data you can use the ``SysClock.now()`` function:


.. :py:func:`SysClock.now()` basic date/time format
 
.. :py:func:`SysClock.today()` more calendar oriented 
 

For example:

>>> from roboclocks import SysClock
>>> sc = SysClock()
>>> sc.now()
2023-08-14 17:28:11 

>>> from robot import Robot
>>> robot = Robot()
>>> robot.sysclock.today()
Mon Aug 14 2023 17:53:49 EDT




