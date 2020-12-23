import bge
from collections import OrderedDict
from mathutils import Vector

class Character(bge.types.KX_PythonComponent):
    args = OrderedDict([
        # definindo opcoens modulares para upbge
        ("Walk Speed", 0.1), 
        ("Run Speed", 0.2), 
        ("Anime idle name:", ""), 
        ("Anime idle S_frame:", 0), 
        ("Anime idle E_frame:", 0)
    ])
    def start(self, args):
        # criando listas de animacoens
        self.idle = (args["Anime idle name:"], args["Anime idle S_frame:"], args["Anime idle E_frame:"])

        # pegando a fisica Character
        self.character = bge.constraints.getCharacter(self.object)

        # pegando velocidades
        self.walkSpeed = args["Walk Speed"]
        self.runSpeed = args["Run Speed"]

    def movement(self):
        # movimentando cubo
        keyboard = bge.logic.keyboard.inputs
        speed = self.walkSpeed
        x = 0
        y = 0
        if keyboard[bge.events.WKEY].active:
            y = 1
        elif keyboard[bge.events.SKEY].active:
            y = -1
        if keyboard[bge.events.EKEY].active:
            x = 1
        elif keyboard[bge.events.QKEY].active:
            x = -1
      
        vec = self.object.worldOrientation * Vector([x, y, 0])
        vec.normalize()  
        self.character.walkDirection = vec * speed
    def update(self):# funcao principal
        self.movement()
