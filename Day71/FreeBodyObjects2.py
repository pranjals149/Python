from math import sin, cos, atan2, radians, degrees, sqrt

class Force:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
        
    def get_horizontal(self):
        horizontal = self.magnitude * cos(self.angle)
        return horizontal

    def get_vertical(self):
        vertical = self.magnitude * sin(self.angle)
        return vertical
        
    def get_angle(self, use_degrees = True):
        if use_degrees == True: return self.angle
        else: 
            pi = 22/7
            radian = self.angle * (pi/180)
            return radian

def find_net_force(lst):
    for i in range(len(lst)):
        total_horizontal = lst[i].get_horizontal
        total_vertical = lst[i].get_vertical
        net_force = (total_horizontal ** 2 + total_vertical ** 2) ** 0.5
        ang = math.atan2(total_vertical, total_horizontal)
    return round(net_force, 1), round(ang, 1)

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())