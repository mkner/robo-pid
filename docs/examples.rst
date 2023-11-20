

Example
-------

Using the module
****************

For example:

>>> import robopid

>>> p = robopid.RoboPid()

Or just:

>>> from robopid import Pid

>>> p = Pid()

>>> p.name()
RoboPid

>>> p.vers()
v0.02.05

>>> p.whoami()
RoboPid v0.02.05 



Mode Examples
*************

The following examples require **robotime**
to be installed for the timing and delay functions.

.. code-block:: console

    $ pip install robo-time

For **robotime** documentation 'see <https://robo-time.readthedocs.io/en/latest/>'_


Getting around...

.. code-block:: python

  from robotime.time import delay
  from robopid import RoboPid
  
  pid = RoboPid()
  
  pid.whoami()
  RoboPid v0.02.06 

  #check default settings
  pid.getGains()
  (1.0, 0, 0)

  pid.setGains(1,0.025,0.0001)

  # check setttings
  pid.getGains()
  (1, 0.025, 0.0001)

  # use integrate mode
  pid.setIntegrateModeOn()

  # check mode flags
  pid.inIntegrateMode()
  True

  pid.inIterateMode()
  False

  # clears previous results, keeps gains intact
  pid.reset()

  #check
  pid.getGains()
  (1, 0.025, 0.0001)

The PID controller automatically calculates the error for the current timestep
that is the difference between the reference signal and the actual process output.
Expressed using standard notation, that is **e(t) = r - y(t)** where **e(t)** is
the error for the  current timestep, **t** is the current timestep, **r** is the
reference signal to track, and **y(t)** is the output at the current timestep
from the process plant.

In **Integrate Mode** the PID controller updates its current output using its
state from previous updates. At each timestep, the three term PID equation
is recalculated. The proportional term is updated using the current error. The
integral term of the PID equation is reintegrated. And the derivative term is
recalculated with respect to the current error. A timestep is the time between
calls to **getPid(...)** or an equivalent. The exact duration of the amount of time
that has passed between consecutive calls is determined by the program that is
using the controller. This is the timestep. It is up to the calling program to
decide how to interpret and utilize the results. Normally this timestep interval 
would be synced to, for instance, the sampling frequency of a device sensor or a 
required control signal update rate for a process device or both. 

Having this mode built into the controller makes it lot easier to concentrate
on tuning the gains of the PID controller and using it to regulate a device and
its applications for tracking, stability and robustness instead of getting
bogged down the intricacies of its mathematical derivations and implementation in code. 
If more specific fine-tuning is needed to the timestep iteration process then the Iterate
Mode can be used


In the following example, the process output is a constant fixed value that
is not and never can be the reference. Shows the effect of timestep
integrations being calculated internally with the PID controller in **Integrative Mode**. 
Expect to see additive integrations gradually increase the PID output, reach the tracking
reference value, then continue to increase without bound since the imaginary process does not react
and a constant, instead of the real output from a process, is fed back into the controller
with each timestep. So its output can never stabilize to the reference, and in this example surpasses it.


.. code-block:: python

  from robotime import delay
  from robopid import RoboPid

  pid = RoboPid()

  # use integrate mode
  pid.setIntegrateModeOn()

  pid.setGains(1,0.025,0.0001)

  # clears previous results, keeps gains intact
  # to start new run
  pid.reset()

  ref_sig = 1.5 # tracking reference signal
  output_sig = 0.5 # output signal or measurement value from the process or device
  
  for i in range(25): 
    pid_out = pid.get(ref_sig, output_sig)
    print(round( pid_out,10))
    delay(500) # more realistic would be 20 ms (50 Hz) instead of 0.5 sec

.. code-block:: python

    1.0126
    1.0375
    1.0625
    1.0875
    1.1125
    1.1375
    1.1625
    1.1875
    1.2125
    1.2375
    1.2625
    1.2875
    1.3125
    1.3375
    1.3625
    1.3875
    1.4125
    1.4375
    1.4625
    1.4875
    1.5125
    1.5375
    1.5625
    1.5875
    1.6125



Repeating the same example above, with the same parameters
but now use **Iterative Mode**

First, set the controller in **Iterate** mode and use the same 
parameters as before.

.. code-block:: python

  # use iterative mode
  pid.setIterateModeOn()

  # not this mode
  pid.inIntegrateMode() # not this mode
  False

  # check really using iterate mode
  pid.inIterateMode()
  True

  pid.reset() # but reuse previous gains
  pid.getGains() # ck ok
  (1, 0.025, 0.0001)

  ref_sig = 1.5 # tracking reference signal
  output_sig = 0.5 # output signal or measurement value from the process or device

Now run the loop. The PID output will fixate at constant value
since there is no integration with the PID timestep outputs. 
In this mode, the integrations would have to handled manually outside of the 
calls to **pid.get(...)** 

.. code-block:: python

  for i in range(10): 
    pid_out = pid.get(ref_sig, output_sig)
    print(round( pid_out,10))
    delay(500) # 0.5 sec 

.. code-block:: python


    1.0126
    0.0249
    0.025
    0.025
    0.025
    0.025
    0.025
    0.025
    0.025
    0.025


A great way to quickly see what type of control is necessary and what
possible complexity will be required of the PID controller for the process device it is being
designed for is to start off with the PID controller in **Integrate Mode**.
Then concentrate on fine tuning the gains. Sometimes this may be enough. If not, 
since there is already working knowledge of the process and it responses, the PID 
controller can be switched into **Iterate Mode** and algorithms and code can be developed
to acheive the optimum required results.

This example repeats the previous one, *but* the  timestep integrations are
handled manually. This allows maximum flexibility to fine-tune the PID 
regulator for the application. 


.. code-block:: python

  #### handle integrations manually

  # use iterative mode
  pid.setIterateModeOn() # use iterate mode

  pid.reset() # 
  pid.getGains() # ck ok

  ref_sig = 1.5 # tracking reference signal
  output_sig = 0.5 # output signal or measurement value from the process or device
  
  pid_out_prev = 0 #need this
  pid_control = 0

Now run the loop. Here, the integrations are handled manually outside of the 
calls to **pid.get(...)** The PID output will match the output when the PID controller 
is set in the automatic **Integrate Mode** as in the first example.


.. code-block:: python

  for i in range(10): 
    
    pid_out = pid.get(ref_sig, output_sig)
    
    # handle the iteration manually
   
    pid_iter = pid_out_prev + pid_out 
    
    # pid_control is the control input u(t) that gets sent to 
    # the process plant either directly or with modifications
    # here just use the plain pid output at this timestep

    pid_control = pid_iter 
    
    print(round( pid_control,10)) # the control input
    
    pid_out_prev = pid_iter 
    delay(500) # more realistic would be 20 ms (50 Hz) instead of 0.5 sec

.. code-block:: python

    1.0126
    1.0375
    1.0625
    1.0875
    1.1125
    1.1375
    1.1625
    1.1875
    1.2125
    1.2375


Wheel-Motor Velocity Controller
*******************************

.. code-block:: python

  #
  #
  #  RoboPid - Python PID Controller for Mobile Robotics
  #
  # example of wheel/motor velocity PID control
  # using controller in timestep iterative mode
  #
  # (c) 2022-2023 - Mike Knerr
  #
  # assume that IoScan is a class that has process thread 
  # input signal processing & buffering capability
  # and a component object of WheelVelocity is clock 
  # that can return the uptime of the clock since
  # instantiation of the WheelVelocity object 
  # in milliseconds with the call clock.millis()
  #
  
  from robotime.clocks import Clock
  from robotime.time import delay 
  from robopid import RoboPid
  
  class WheelVelocity(IoScan):
  
      def __init__(self, wheel):#, velocity):
          super(WheelVelocity, self).__init__()
  
          self._name = "WheelVelocity"
          self._desc = "WheelVelocity"
          self._vers = "v0.01.02"  # x,y.02 for RoboPid
          self._wheel = wheel #construct with existing active wheel object
          
          self.pid = RoboPid() # on ext interface
          self.clock = Clock() # uptime & timing clock 
          
          self._v_ref = 0 # signal reference velocity
          self._v = 0 # current instantaneous velocity
          self._v_avg = 0
          
          self._pid_out = 0
          self._pid_out_prev = 0
          
          self._rate = 0
          self._rate_prev = 0
          self._rate_pid = 0
      
          self._vmax = 0.50 # max velocity (m/s) of wheels 
          
          self._default_scanfreq = 50
          self._default_bufsize = 5
          # clock from IoScan
          # used in interation process thread
          self._dur_start_time = self.clock.millis()
          self._dur = None
       
          #init
          #self.deActivate()
          self.stopScanning()
          self.setScanFreq(self._default_scanfreq)
          self.setBufferingOff()
          self.setBufSize(self._default_bufsize)
          self.setBufferingOn()
          #important
          self.pid.setIterateModeOn()
          self.startScanning()
          
  #
  # this function would be called every self.getTimeinc() timesteps
  # by a process thread that is running in the WheelVelocity object
  #
  
      def _velocity_handler(self):
          
          # else process signal
        
          #ok, use ONLY this call from WheelVelocity object
          self._v =  self._wheel._velocity._getVelocityGo()
        
          if self.isBuffering():
                if len(self._buf) > 0 \
                    and self._v != None: #be robust
                  self._buf.pop(0)
                  self._buf.append(self._v)
                ## ok
                self._v_avg  = self.getBufAvg()
          else:
              # really want to use  buffered velocity, 
              self._v_avg = self._v
              
          #set timestep always, it can change dynamically
          time_inc_sec = self.getTimeinc()/1000 # in seconds to match meters/sec
          self.pid.setTimeinc(time_inc_sec)
          
          if self._v_ref > 0:
              self._pid_out = self.pid.getPid(self._v_ref, self._v_avg) #,time
          
          if self._v_ref < 0:
              self._pid_out = self.pid.getPid(abs(self._v_ref), abs(self._v_avg)) #,time
          
          # similar to technique used w/ stanley AV simulator
          # for throttle control signal
          # pid in iterative mode for timestep discretized version
          self._rate_pid = self._rate_prev + self._pid_out
          
          # rate is a speed, not a vector like velocity
          # so it is always constrained in [1,100]
          
          # if there is an active signal
          # zero is no active signal
          
          if self._v_ref > 0:
              self._rate = constrain(self._rate_pid,0,100)
              # or in [1,100]
              #self._rate = constrain(self._rate_pid,1,100)
             
              if self._rate >0:
               self._wheel.forward(self._rate)
           
           # if there is an active signal
          if self._v_ref < 0: 
              # or in [1,100]
              #self._rate = constrain(self._rate_pid,1,100)
              #use abs of pid out for v reg <0 ?
              self._rate = constrain(self._rate_pid,0,100)
              
              if self._rate >0:
               self._wheel.reverse(self._rate)
               
          self._rate_prev = self._rate 
              
          ##########################################
              
          if self._dur != None:
            if (self.clock.millis() - self._dur_start_time) > self._dur:
                self._wheel.stop()
                self._dur = None
  
          return
      

