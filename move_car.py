directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}


# i think this is where you're trying to define the grid,
# but you don't specify what kind of input you're asking for
# or what limits on that input would be
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

# don't define these out here - put within the class
first_vehicle_x = None
first_vehicle_y = None

# dir is a built-in function; use a unique variable name (e.g., face)
# not clear why you have 'face' but then re-name it; pick one
class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face
# verify input  - self.dir can only be 'N', 'S','E', or 'W'
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

# test - i don't think this will move the vehicle one step in the given direction;
# instead looks like it'll just override the starting location with any
# possible location
# e.g., if starting at (0,0) on the grid and want to move north,
# car.move(2,1) will move you to position (2,3), which is NE
    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

# how does the function know what first_vehicle_x/y is? 
# what happens if these conditions aren't met?
# what if there are more than 2 cars, or you're moving the first vehicle
# because first_vehicle_x defined as global variable, will always be none

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y


# what input are you asking for? how does the user know what to provide?
# looks like they need to be instructed to give at least 3 inputs (x,y,direction)
vehicle_one_pos = raw_input().split()

# same; user doesn't know what you want. need to specify L, R, M
vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])

# write as a function instead of using eval
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))


first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

# same as above; input isn't clear.
vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

# the "fixed code" commit created a typo - should be 'vehicle_two_pos[2]'
vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir

