**robo-pid** 

A Python PID Controller For Mobile Robotics

**RoboPID** is PID controller designed to handle the combined kinematic 
and dynamic complexity of mobile robotics. The controller implements timestep
integration and can be used in discretized time regulators.


**RoboPID** has proven to be a tested, reliable PID controller that can
regulate the dynamic balance and rapid response required for differential drive
linear and lateral wheeled motion control. It has been used, for example with mobile
robotic systems for LVC (Linear Velocity Control) for regulating wheel velocities, 
LVDR (Lateral Velocity Differential Regulator) for keeping the wheel velocities in sync for 
differential drive mobile robots when traversing a straight line path and 
ADVR (Angular Differential Velocity Regulator) for tracking a heading angle using typical
motion control input signals (v,w) for linear velocities and angular orientation rotational rates.


The PID controller supports 2 modes of operation: **Integrative** and **Iterative**

In **Integrative Mode**, the timestep integrations are calculated inside the controller
and the output from the PID controller for the current timestep is used directly or with 
modifications and sent to the device or process plant as the current input signal without
further iterative integration.

In **Iterative Mode**, the PID timestep integrations are manually calculated and updated
outside the controller in the algorithm that calls the PID controller for the output of
the PID at the current timestep.


Installation: 

$ **pip** install robo-pid

For documentation see https://robo-pid.readthedocs.io/en/latest/





