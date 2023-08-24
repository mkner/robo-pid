Basic PID -

A Python PID controller for discretized time calculations

Basic PID is a classic PID controller that is easy to use, works and does the job.

The PID controller implements timestep integration
that is designed to be used in discretized time regulators.

Basic PID has proven to be a tested, and reliable PID controller. It has been used,
for example, with mobile robotic systems for LVC (linear velocity control) for wheels,
LVDR (lateral velocity differential regulator) and ADVR (angular differential velocity
regulator) for tracking a heading angle with differential drive robots using typical
motion control input signals for linear & angular velocities.

It supports 2 modes of operation: Integrative and Iterative

In iterative mode, the timestep integration for updating an input
signal is done in the algorithm that calls the PID controller
for the ouput of the PID at the current timestep.

In integrative mode, the timestep integration is done inside the
controller and the output from the PID controller for the
current timestep is used directly to be sent to the process plant
as the current input signal.

For documentation see https://basic-pid.readthedocs.io/en/latest/





