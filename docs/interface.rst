
Interface
---------

.. class:: RoboPid()

  
 .. method:: setGains(Kp,Ki,Kd)
        
    sets the gains:

     | Kp - proportional gain
     | Ki - integral gain
     | Kd - derivative gain

   :param: Kp - proportional gain
   :param: Ki - integral gain
   :param: Kd - derivative gain
   :return: None


 .. method:: getGains()

    get the currently set gains 

    | Kp - proprotional gain
    | Ki - integral gain
    | Kd - derivative gain

    :return: (Kp, Ki, Kd)
    :rtype: tuple


 .. method:: setKp(Kp)
 
    sets the proportional gain **Kp**

    :param: Kp - the proportional gain


 .. method:: getKp()

    get the current proportional gain **Kp**
 
    :return: Kp
    :rtype: float


 .. method:: setKi(Ki)

    sets the integral gain **Ki**

    :param: Ki - the integral gain


 .. method:: getKi()

    get the current integral gain **Ki**

    :return: Ki
    :rtype: float


 .. method:: setKd(Kd):

    sets the derivative gain **Kd**

    :param: Kd - the derivative gain


 .. method:: getKd()

    get the current derivative gain **Kd**
    
    :return: Kd 
    :rtype: float


 .. method:: setIntegrateModeOn()

    Turns integrative mode on

    In integrative mode, the timestep integrations are calculated inside the
    controller and the output from the PID controller for the current timestep
    is used directly or with modifications and sent to the device or process
    plant as the current input signal. The integrations are cumulative across 
    all timesteps until the PID controller is restarted with **reset()** or **resetAll()**

    :param: None
    :return: None


 .. method:: setIterateModeOn()

   Turns iteration mode on

    In iterative mode, the PID timestep integrations are manually calculated
    and updated outside the controller in the algorithm **that calls** the
    PID controller for the output of the PID at the current timestep. The output of
    the PID is localized to **this** timestep and not cumulative across all calls for
    the PID output since the start or restart of the controller by calling **reset()** 
    or **resetAll()**. The accumulative effect of the PID is handled by the functional 
    algorithm that is using the PID controller and then sent to the device or
    process plant as an input signal. 
    
   :param: None
   :return: None


 .. method:: inIntegrateMode()

    check if using integrative mode for PID evaluation

    :return: **True** if in integrative mode and **False** if not
    :rtype: Bool


 .. method:: inIterateMode()

    check if using iterative mode for PID evaluation

    :return: **True** if in iterative mode and **False** if not
    :rtype: Bool


 .. method:: setTimeinc(time_inc)

    Sets the discrete timestep increment value used in integrative
    calculations. **time_inc** can be any positive value.  Set the **time_inc** unit
    of measurement to be the same unit as the sample rate of current signal. This 
    value can be changed dynamically while the controller is running to adjust to 
    changes in the frequency of the input signal if necessary.

   :param: time_inc
   :return: None


 .. method:: getTimeinc()

    returns the current discrete timestep increment value

    :param: None
    :return: time_inc
   

 .. method:: getPid(signal_ref, signal)

   Returns the results of the PID equation evaluation **since the last** call
   to this function. It is usually called at each timestep interval that is
   synced to the measured signal that samples at the same timestep
   interval frequency. Calculation, accumulative and persistent values 
   depend on the mode setting.
   
  
   :param: signal_ref - reference signal value
   :param: signal  - current measured signal value returned by process 
   :return: result of PID equation eval
   :rtype: float


 .. method::  getPidTuple(signal_ref, signal)
    
    Returns tuple form of the components of the PID equation
    *since last evaluation* that was initiated by calling **getPid(...)** or 
    an equivalent. 
    
    :param: signal_ref - reference signal value
    :param: signal  - current measured signal value
    :return: components of PID equation evaluation (Kp P, Ki, I, Kd, D)

     |  Kp - proprotional gain
     |  P  - result of proportional term evaluation
     |  Ki - integral gain
     |  I  - result of integral term evaluation
     |  Kd - derivative gain
     |  D  - result of derivative term evaluation

   :rtype: tuple


 .. method::  pid(signal_ref, signal)
   
    short form for **getPid(...)**
    

 .. method::  get(signal_ref, signal)

    short form for **getPid(...)**



 .. method:: reset()

  Resets the controller for a new run. Clears out integration
  results but keeps the currently set gains and mode parameters intact.

  :param: None
  :return: None


 .. method:: resetAll()
       
  Resets all runtime variables to the the object instance 
  initialization state.  Gains and timestep increment values are also
  set to default values. Previous integration results are cleared.

  :param: None
  :return: None


