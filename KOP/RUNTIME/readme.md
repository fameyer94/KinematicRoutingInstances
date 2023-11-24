# Problem instances for hyperparameter tuning
The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate SPACE priority

This is a description of the problem instances generated for hyperparameter tuning. For all instances, each waypoint (x-coordinate,y-coordinate) is sampled randomly with x \in [0, 10], y \in [0, 10]. The priority is randomly sampled within the interval [0, 9]. The first entry represents the start waypoint, the last entry represents the end waypoint. Start and end waypoint are assigned the priority zero.

## Detailed description of each instance:
- 5a/b/c/d/e.txt: test instance with 5 randomly sampled waypoints
- 10a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 15a/b/c/d/e.txt: test instance with 15 randomly sampled waypoints
- 20a/b/c/d/e.txt: test instance with 20 randomly sampled waypoints
- 25a/b/c/d/e.txt: test instance with 25 randomly sampled waypoints

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
