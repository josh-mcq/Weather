import numpy as np

class motor(name):
    def __init__(self):
        self.name = name
    def intensity(self, distance_from_focal, ):


class buzz():
    def __init__(self):
        self.motor_one = self.motor("one")
        self.motor_two = self.motor("two")
        self.motor_three = self.motor("three")
        self.motor_four = self.motor("four")

    def focal_point_generator(self, clip_rate):
        '''
        This is a generator that will yield a constant stream of data
        something will keep calling "next" on it, and it will keep yielding one sin val at a time
        '''
        time = np.arange(0,10,0.1)  # this represents all the values of the x axis, and is thus, infinite.
        # the base_amplitude will be a sin wave of amplitude values representing the movement of the focal
        # away from it's center point
        base_amplitude = np.sin(time)
        i = 0
        while True:
            yield np.sin(i)
            i += 0.1

def main():
    # this is where the main loop is going to run indefinitely
    # or does this just return things to the .ino file?  IDK!

if __name__ == '__main__':
    main()



