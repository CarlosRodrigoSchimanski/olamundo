import bge
from collections import OrderedDict

class Armature(bge.types.KX_PythonComponent):
    args = OrderedDict([

    ])
    def start(self, args):
        pass

    def update(self):
        parent = self.object.parent
        character = bge.constraints.getCharacter(parent)
        direction = character.walkDirection
        self.object.alignAxisToVect(direction, 2 , 0.8)
        self.object.alignAxisToVect([0,0,1], 2, 1)
        
