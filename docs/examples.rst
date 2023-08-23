

Example
------------

To use this project, first install it using pip:

.. code-block:: console

    $ pip install roboclocks



To get current time and date info based on the current underlying 
system OS/HW configuration for place/timezone you can use several 
functions 


For example: basic numeric date/time data

you can use the ``SysClock.now()`` function:

.. autofunction:: SysClock.now()
.. autofunction:: SysClock.today()
.. autofunction:: SysClock.date()

 :py:func:`SysClock.now()` basic date/time format
 :py:func:`SysClock.today()` more calendar oriented

 :py:func:`SysClock.today()` friendlier

 :py:func:`object.function`does something


For example:

>>> from roboClocks import SysClock
>>> sc = SysClock()
>>> sc.now()
2023-08-14 17:28:11 

>>> from robot import Robot
>>> robot = Robot()
>>> robot.sysclock.today()
Mon Aug 14 2023 17:53:49 EDT




