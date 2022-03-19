# Author: Blake Ballew
# Description: class representing the roundabout itself

from car import car

class roundabout:
    def __init__(self):
        
        # "jump starts" the simulation by initializing roundabout with 4 cars all set to immediately exit
        # hence we need to offset the flow to -4
        self.flow = -4
        self.structure = [car(True), car(True), car(True), car(True)]
    
    def iterate(self, P):
        self.structure.insert(0, self.structure.pop())
        for x in range(4):
            self.structure[x].passed += 1
            if self.structure[x].exists:
                if self.structure[x].passed == self.structure[x].exit:
                    self.flow += 1
                    self.structure[x].exists = False
            if not self.structure[x].exists:
                self.structure[x] = car(False, P)

    def show(self):
        print([self.structure[0].contents(), self.structure[1].contents(), 
                self.structure[2].contents(), self.structure[3].contents()])