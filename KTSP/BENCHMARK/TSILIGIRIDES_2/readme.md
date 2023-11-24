# Modified Tsiligirides Dataset 2
This is a description of the problem instances from the Tsiligirides dataset 2.
All problem instances were dropped the restriction of a maximum path length and the priority assigned to each waypoint, since both is not relevant for the TSP-model. Further, no explicit start and end node is defined, sind in the TSP case a Hamiltonian cycle is seeked.

The resulting instance under investigation are as follows:
- Tsiligirides2_025: x and y coordinate of each waypoint scaled by the factor 0.25
- Tsiligirides2_050: x and y coordinate of each waypoint scaled by the factor 0.50
- Tsiligirides2_100: x and y coordinate of each waypoint scaled by the factor 1.00
- Tsiligirides2_200: x and y coordinate of each waypoint scaled by the factor 2.00
- Tsiligirides2_400: x and y coordinate of each waypoint scaled by the factor 4.00

All problem instances where solve with the following kinematic restirctions:
- v_max = 3 m/s
- a_max = 1.5 m/s^2

The structure of the file is as follows: 

waypoint_id SPACE x-coordinate SPACE y-coordinate