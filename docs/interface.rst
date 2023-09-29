
Interface
---------

.. class:: BasicPid()


 .. method:: reset()

  Resets for new controller run. Clears out integrations
  but keeps gains intact.


 .. method:: resetAll()
       
  Resets all internal variables to the the object instance 
  initialization state. Gains & timestep increment are also
  set to default values.

 .. method:: setIntegrateModeOn()

 Sets integrative mode on

 .. method:: setIterateModeOn()

 Sets iteration mode on

 .. method:: inIntegrateMode()

   returns True if in integrative mode and False if not


 .. method:: inIterateMode()

   returns True if in iteration mode and False if not


 .. method:: setTimeinc(time_inc)

    Sets the discrete timestep increment value used in integrative
    calculations. **time_inc** can be any positive value  The **time_inc** unit
    of measurement needs to be the same unit as the sample rate of 
    current signal. This value can be changed dynamically while the controller is running.

 .. method:: getTimeinc()

   returns the current discrete timestep increment value


 .. method:: setGains(Kp,Ki,Kd)
        
      sets the gains:

        Kp - proportional gain

        Ki - integral gain

        Kd - derivative gain


 .. method:: getGains()

      returns the tuple (Kp, Ki, Kd)


 .. method:: setKp(Kp)

        sets Kp


 .. method:: getKp()

        returns Kp   


 .. method:: setKi(Ki)

        sets Ki


 .. method:: getKi()

     returns Ki


 .. method:: setKd():

       sets Kd


 .. method:: getKd()

        returns Kd


 .. method:: getPid(signal_ref, signal)

    signal_ref - reference signal value

    signal  - current measured signal value

   Returns the results of the PID equation evaluation since the last call
   to this function. It is usually called each time_step interval that is
   also synced to the measured signal that samples at the same time interval
   Calculation & persistent values depend on mode


 .. method::  getPidTuple(signal_ref, signal)

    returns tuple form of the components of the PID
    equation evaluation irregardless of mode

    (Kp P, Ki, I, Kd, D)


 .. method::  pid(signal_ref, signal)

   short form for getPid(signal_ref, signal)


 .. method::  get(signal_ref, signal)

   short form for getPid(signal_ref, signal)



