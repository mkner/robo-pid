
Interface
---------

.. class:: BasicPid()


 .. method:: reset()

  Resets for new controller run. Clears out integrations
  but keeps gains intact

  :param: None
  :return: None

 .. method:: resetAll()
       
  Resets all internal variables to the the object instance 
  initialization state. Gains & timestep increment are also
  set to default values.

  :param: None
  :return: None

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
    calculations. **time_inc** can be any positive value  Set the **time_inc** unit
    of measurement to be the same unit as the sample rate of current signal. This 
    value can be changed dynamically while the controller is running to adjust to 
    changes in the frequency of the input signal if necessary.

   :param: time_inc
   :return: None


 .. method:: getTimeinc()

     returns the current discrete timestep increment value

   :param: None
   :return: time_inc
   
  
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


 .. method:: setKd(Kd):

       sets Kd


 .. method:: getKd()

        returns Kd


 .. method:: getPid(signal_ref, signal)

   Returns the results of the PID equation evaluation *since the last* call
   to this function. It is usually called each **time_step** interval that is
   also synced to the measured signal that samples at the same time interval
   Calculation & persistent values depend on mode
  
   :param: signal_ref - reference signal value
   :param: signal  - current measured signal value
   :return: result of PID equation eval
   :rtype: float


 .. method::  getPidTuple(signal_ref, signal)
    
    returns tuple form of the components of the
    PID equation evaluation irregardless of mode
    
   :param: signal_ref - reference signal value
   :param: signal  - current measured signal value
   :return: components of PID equation evaluation (Kp P, Ki, I, Kd, D)

            Kp - proprotional gain
            P  - result of proportional term evaluation
            Ki - integral gain
            I  - result of integral term evaluation
            Kd - derivative gain
            D  - result of derivative term evaluation

   :rtype: tuple

 .. method::  pid(signal_ref, signal)
   
   short form for getPid(signal_ref, signal)
    

 .. method::  get(signal_ref, signal)

   short form for getPid(signal_ref, signal)



