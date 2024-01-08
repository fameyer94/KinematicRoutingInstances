# Problem instances for hyperparameter tuning
This is a description of the problem instances generated for hyperparameter tuning. For all instances, each waypoint (x,y) is sampled randomly with x \in [0, 20], y \in [0, 20].

## Detailed description of each instance:
- hpt_test10: test instance with 10 randomly sampled waypoints
- hpt_test15: test instance with 15 randomly sampled waypoints
- hpt_test20: test instance with 20 randomly sampled waypoints
- hpt_test25: test instance with 25 randomly sampled waypoints
- hpt_test30: test instance with 30 randomly sampled waypoints
- hpt_test35: test instance with 35 randomly sampled waypoints


## All problem instances were solved with the following kinematic restrictions:
- v_max = 3 m/s //overall maximum velocity
- a_max = 1.5 m/s^2 //overall maximum acceleration

## Set of possible traversal velocities for each node
- V = {0.0, 0.2*v_max/sqrt(2), 0.4*v_max/sqrt(2), 0.6*v_max/sqrt(2), 0.8*v_max/sqrt(2), 1*v_max/sqrt(2)}  (m/s)
- sqrt(2) = 1.4142...

## Set of possible traversal heading angles for each node
- H = {0.0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4}  (rad)
- pi = 3.1415...

The structure of the file is as follows: 

waypoint_id SPACE x-coordinate SPACE y-coordinate