# Author: Blake Ballew
# Description: car class containing properties of the cars present in the roundabout
import random

class car:
    def __init__(self, initialize, P=100):
        self.exists = False
        self.passed = 0
        if not initialize:
            self.exit = random.randint(1,3)
            if random.randint(1,100) < P:
                self.exists = True
        else:
            self.exists = True
            self.exit = 1

    def contents(self):
        return [self.exists, self.exit, self.passed]