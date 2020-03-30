# randomwalk
#random walk
from random import choice

class RandomWalk():
    """A class to generate random walk"""
    def __init__(self,num_points=50000):
        """initialize the attributes of a walk"""
        self.num_points=num_points
        #all walk starts at (0,0)
        self.x_values=[0]
        self.y_values=[0]
    #step direction and distance
    def fill_walk(self):
        """calculate all the points in the walk"""
        #keeping track until the walk reaches to the desired length
        while(len(self.x_values)<self.num_points):
            #decide the direction
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance # 0 makes it to move verticaly
            y_direction=choice([-1,1])
            y_distance=choice([-0,1,2,3,4])
            y_step=y_direction*y_distance #0 makes to move horizontally
        #reject moves to go nowhere
            """ when bith x and y step becomes 0, loop gets continued"""
            if x_step==0 and y_step==0:
                continue
            
            next_x=self.x_values[-1]+x_step
            #adds x step to last stored value of x
            next_y=self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
              
