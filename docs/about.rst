
About
*****

A Python PID controller for discrete time regulators

**Basic PID** is a classic PID controller that is easy to use, works and does the job.

The controller implements timestep integration that is designed to be used in discretized time regulators.

**Basic PID** has proven to be a tested, and reliable PID controller. It has been used, for example, with mobile robotic systems for LVC (Linear Velocity Control) for regulating wheel velocities, LVDR (Lateral Velocity Differential Regulator) for keeping the wheel velocities in sync for differential drive mobile robots when traversing a straight line path and ADVR (Angular Differential Velocity Regulator) for tracking a heading angle using typical motion control input signals (v,w) for linear & angular velocities.

There are 2 primary modes of operation:  **Integrative** and **Iterative**

In **iterative mode**, the timestep integration is done outside the controller
in the algorithm *that calls* the PID controller for the ouput of the PID at the current timestep.

In **integrative mode**, the timestep integration is done *inside* the controller and the output from the PID controller for the current timestep can be used directly, without further iterative integration, to be sent to the process plant as the current input signal or as a modified signal depending on the feedback system in use.

