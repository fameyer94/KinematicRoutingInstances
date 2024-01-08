# Tsiligirides dataset 3.
This is a description of the problem instances from the Tsiligirides dataset 3.

The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate SPACE priority

The resulting problem instances under investigation are as follows:
- Tsiligirides3.txt: Original Tsiligirides dataset 3 instance

## All problem instances were solved with the following kinematic restrictions:
- v_max = 3 m/s //overall maximum velocity
- a_max = 1.5 m/s^2 //overall maximum acceleration

## Set of possible traversal velocities for each node
- V = {0.0, 0.2*v_max/sqrt(2), 0.4*v_max/sqrt(2), 0.6*v_max/sqrt(2), 0.8*v_max/sqrt(2), 1*v_max/sqrt(2)}  (m/s)
- sqrt(2) = 1.4142...

## Set of possible traversal heading angles for each node
- H = {0.0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4}  (rad)
- pi = 3.1415...

## Travel time budgets:
The travel time budget is specified within the thesis!