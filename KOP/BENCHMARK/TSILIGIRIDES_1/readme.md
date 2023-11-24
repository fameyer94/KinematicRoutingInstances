# Tsiligirides Dataset 1
This is a description of the problem instances from the Tsiligirides dataset 1.

The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate SPACE priority

The resulting instance under investigation are as follows:
- Tsiligirides1.txt: Original Tsiligiri dataset 1 instance

## Properties applied for hyperparaemter tuning
### All problem instances where solve with the following kinematic restirctions:
- v_max = 3 m/s //overall maximum velocity
- a_max = 1.5 m/s^2 //overall maximum acceleration

### Set of possible traversal velocities for each node
- V = {0.0, 0.2*v_max/sqrt(2), 0.4*v_max/sqrt(2), 0.6*v_max/sqrt(2), 0.8*v_max/sqrt(2), 1*v_max/sqrt(2)}  (m/s)
- sqrt(2) = 1.4142...

### Set of possible traversal heading angles for each node
- H = {0.0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4}  (rad)
- pi = 3.1415...

### Travel time budgets:
The travel time budget is specified within the thesis!