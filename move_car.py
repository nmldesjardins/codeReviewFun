directions = ['N','E','S','W'] 
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}



gridMaxX, GridMaxY = raw_input("Enter X and Y separated by a space:").split()


class Vehicle():
    cardDir = ['N','E','S','W'] 
    movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.face = cardDir.index(face)

    def turn_left(self):
        self.face = cardDir[(cardDir.index(self.face)-1)%len(cardDir)]

    def turn_right(self):
        self.dir = cardDir[(cardDir.index(self.dir)+1)%len(cardDir)]

    def move_one(self):
        if self.face == 'N': 
            new_y = self.y + 1
        elif self.face =='S':
            new_y = self.y - 1
        elif self.face == 'E':
            new_x = self.x + 1
        else: 
            new_x = self.x - 1
    
    def move_anywhere(self,direction,steps):
        allMove = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0),
                    'NE':(1,1), 'SE':(1,-1), 'NW': (-1,1), 'SW': (-1,-1)
        }
        new_x = self.x + allMove[direction][0] + steps
        new_y = self.y + allMove[direction][1] + steps
        


# what input are you asking for? how does the user know what to provide?
# looks like they need to be instructed to give at least 3 inputs (x,y,direction)
vehicle_one_pos = raw_input("Give starting position (x y direction):").split()

# same; user doesn't know what you want. need to specify L, R, M
vehicle_one_commands = raw_input("Give command (L, R, or M):")

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])


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

