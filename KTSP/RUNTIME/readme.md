# Problem instances for the run time analysis
This is a description of the problem instances generated for analysis of the runtimes of the approaches used in my PhD thesis. For all instances, each waypoint (x,y) is sampled randomly with x \in [0, 20], y \in [0, 20].

The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate

## Detailed description of each instance:
- 10a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 12a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 14a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 16a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 18a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 20a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 22a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 24a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 26a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 28a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 30a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 32a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 34a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 36a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 38a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 40a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints

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

