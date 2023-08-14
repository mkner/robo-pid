Usage
=====

.. _installation:

Installation
------------

To use this project, first install it using pip:

.. code-block:: console

    $ pip install roboclocks

example heading
----------------

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

>>> import SysClock
>>> sysclock = SysClock()
>>> sysclock.now()
2023-08-14 17:28:11 

>>> robot.sysclock.today()
Mon Aug 14 2023 17:53:49 EDT




