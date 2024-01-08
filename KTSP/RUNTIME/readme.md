# Problem instances for the run time analysis
This is a description of the problem instances generated for analysis of the runtimes of the approaches used in my Ph.D. thesis. For all instances, each waypoint (x,y) is sampled randomly with x \in [0, 20], y \in [0, 20].

The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate

## Detailed description of each instance:
- 10a/b/c/d/e.txt: test instance with 10 randomly sampled waypoints
- 12a/b/c/d/e.txt: test instance with 12 randomly sampled waypoints
- 14a/b/c/d/e.txt: test instance with 14 randomly sampled waypoints
- 16a/b/c/d/e.txt: test instance with 16 randomly sampled waypoints
- 18a/b/c/d/e.txt: test instance with 18 randomly sampled waypoints
- 20a/b/c/d/e.txt: test instance with 20 randomly sampled waypoints
- 22a/b/c/d/e.txt: test instance with 22 randomly sampled waypoints
- 24a/b/c/d/e.txt: test instance with 24 randomly sampled waypoints
- 26a/b/c/d/e.txt: test instance with 26 randomly sampled waypoints
- 28a/b/c/d/e.txt: test instance with 28 randomly sampled waypoints
- 30a/b/c/d/e.txt: test instance with 30 randomly sampled waypoints
- 32a/b/c/d/e.txt: test instance with 32 randomly sampled waypoints
- 34a/b/c/d/e.txt: test instance with 34 randomly sampled waypoints
- 36a/b/c/d/e.txt: test instance with 36 randomly sampled waypoints
- 38a/b/c/d/e.txt: test instance with 38 randomly sampled waypoints
- 40a/b/c/d/e.txt: test instance with 40 randomly sampled waypoints

## All problem instances were solved with the following kinematic restrictions:
- v_max = 3 m/s //overall maximum velocity
- a_max = 1.5 m/s^2 //overall maximum acceleration

## Set of possible traversal velocities for each node
- V = {0.0, 0.2*v_max/sqrt(2), 0.4*v_max/sqrt(2), 0.6*v_max/sqrt(2), 0.8*v_max/sqrt(2), 1*v_max/sqrt(2)}  (m/s)
- sqrt(2) = 1.4142...

## Set of possible traversal heading angles for each node
- H = {0.0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4}  (rad)
- pi = 3.1415...

