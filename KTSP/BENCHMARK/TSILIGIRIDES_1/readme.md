# Modified Tsiligirides Dataset 1
This is a description of the problem instances from the Tsiligirides dataset 1.
All problem instances drop the restriction of a maximum path length and the priority assigned to each waypoint since both are irrelevant to the TSP-model. Further, no explicit start and end node is defined, since in the TSP case a Hamiltonian cycle is sought.

## The resulting problem instances under investigation are as follows:
- Tsiligirides1_025: x and y coordinate of each waypoint scaled by the factor 0.25
- Tsiligirides1_050: x and y coordinate of each waypoint scaled by the factor 0.50
- Tsiligirides1_100: x and y coordinate of each waypoint scaled by the factor 1.00
- Tsiligirides1_200: x and y coordinate of each waypoint scaled by the factor 2.00
- Tsiligirides1_400: x and y coordinate of each waypoint scaled by the factor 4.00

## All problem instances were solved with the following kinematic restrictions:
- v_max = 3 m/s
- a_max = 1.5 m/s^2

## The structure of the file is as follows: 
waypoint_id SPACE x-coordinate SPACE y-coordinate