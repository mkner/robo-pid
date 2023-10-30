

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
'...'

>>> p.vers()
'...'

>>> p.desc()
'...'


Wheel-Motor Velocity Controller
*******************************

.. code-block:: python

  # example of wheel/motor velocity PID control
  # using BasicPid in timestep iterative mode
  # assume that IoScan is a class that has background process
  # input signal processing & buffering capability
  # and a component object of WheelVelocity is clock 
  # that can return the uptime of the clock since
  # instantiation of the WheelVelocity object 
  # in milliseconds with the call clock.millis()
  #
  # (c) 2023, 2022 - Mike Knerr
  #

  from robotime.clocks import Clock
  from basicpid import BasicPid
  

  class WheelVelocity(IoScan):

    def __init__(self, wheel):
        super(WheelVelocity, self).__init__()

        self._name = "WheelVelocity"
        self._desc = "WheelVelocity"
        self._vers = "v0.01.02"  # 0.09 w/ velocity

        self._wheel = wheel #contains motor 
        self.clock = Clock()

        self.pid = BasicPid() # on ext interface
        
        self._v_ref = 0 # signal reference velocity
        self._v = 0 # current instantaneous velocity
        self._v_avg = 0
        
        self._pid_out = 0
        self._pid_out_prev = 0
        
        self._rate = 0
        self._rate_prev = 0
        self._rate_pid = 0
    
        self._vmax = 0.50 # of wheels/motors
        
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
        

     # this function would be called every self.getTimeinc() timesteps
     # by a process thread that is running in the WheelVelocity object
     # handled by class IoScan that WheelVelocity is decendant from

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
        time_inc_sec = self.getTimeinc()/1000
        self.pid.setTimeinc(time_inc_sec)
        
        if self._v_ref > 0:
            self._pid_out = self.pid.getPid(self._v_ref, self._v_avg) #,time
        
        if self._v_ref < 0:
            self._pid_out = self.pid.getPid(abs(self._v_ref), abs(self._v_avg)) #,time
        
        # similar to technique used w/ stanley simulator
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
            #USE THE ABS OF PID OUT FOR v_reg < 0 ?
            self._rate = constrain(self._rate_pid,0,100)
            
            if self._rate >0:
             self._wheel.reverse(self._rate)
             
        self._rate_prev = self._rate 
            
        if self._dur != None:
          if (self.clock.millis() - self._dur_start_time) > self._dur:
              self._wheel.stop()
              self._dur = None
        return
    







