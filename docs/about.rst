
About
*****

**robo-pid** 

A Python PID Controller For Mobile Robotics

**RoboPID** is a PID controller designed for Autonomous Mobile Robotics 
to handle the combined kinematic and dynamic complexity of differential
drive linear and lateral wheeled motion control. The controller implements
timestep integration and can be used in discretized time regulators.

**Robo PID** has proven to be a tested, and reliable PID controller. It has been used, for example, 
with mobile robotic systems for LVC (Linear Velocity Control) for regulating wheel velocities, 
LVDR (Lateral Velocity Differential Regulator) for keeping the wheel velocities in sync for 
differential drive mobile robots when traversing a straight line path and 
ADVR (Angular Differential Velocity Regulator) for tracking a heading angle using typical
motion control input signals (v,w) for linear velocities & angular orientation rotational rates.

The PID controller supports 2 modes of operation: **Integrative** and **Iterative**

In **integrative mode**, the timestep integrations are calculated inside the controller
and the output from the PID controller for the current timestep is used directly or with
modifications and sent to the device or process plant as the current input signal.

In **iterative mode**, the PID timestep integrations are manually calculated and updated
outside the controller in the algorithm that calls the PID controller for the output of
the PID at the current timestep. 

