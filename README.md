# codeReviewFun

This is an excercise in code review taken from http://codereview.stackexchange.com/questions/155913/create-two-vehicles-move-them-on-a-grid-based-on-user-input


## Directions
* Fork repository
* clone to your desktop
* make changes all in one file
* merge to your fork
* discuss with your group! 

I have a grid and a class Vehicle, which will have starting point(X, Y on the grid) and direction(one of N,E,S,W) taken from user and there will be commands, L & R turns the vehicle 90 degrees around left and right respectively and M moves the vehicle one unit to faced direction.

For instance, if the command is M and the current direction is E, the vehicle moves from (x,y) to (x+1,y) and preserve its direction.
If the command is R, and the current direction is E, vehicle preserves its position but direction changes to S.

My input consists of 5 lines:

The first line defines the limits of the grid; X and Y separated by space
The second line defines the current position and facing direction for the first vehicle; X, Y and Dir are separated by space
The third line defines the commands for the first vehicle, which is a line of string
The fourth and fifth lines are the same as second and third except they are for the second vehicle
Note: Vehicles are sent sequentially. If the second vehicle attempts to move to the occupied spot of the first vehicle, the command will be skipped. If any move command makes any of the vehicles move out of the grid, that command will be skipped as well. Inputs are always in expected style, so there is no need to validate inputs.
