import bge
from collections import OrderedDict
from mathutils import Vector

class Character(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ("Walk Speed", 0.1), 
        ("Rot speed", 0.2), 
        ("Armature name:", ""),
        ("Anime idle name:", ""), 
        ("Anime idle S_frame:", 0), 
        ("Anime idle E_frame:", 0), 
        ("Anime idle priorit:", 0),
        ("Anime run name:", ""), 
        ("Anime run S_frame:", 0), 
        ("Anime run E_frame:", 0), 
        ("Anime run priorit:", 0)
    ])
    def start(self, args):
        # criando listas de animacoens
        self.idle = (args["Anime idle name:"], 
        args["Anime idle S_frame:"], 
        args["Anime idle E_frame:"], 
        args["Anime idle priorit:"])

        self.run = (args["Anime run name:"], 
        args["Anime run S_frame:"], 
        args["Anime run E_frame:"], 
        args["Anime run priorit:"])

        # pegando a fisica Character
        self.character = bge.constraints.getCharacter(self.object)
        
        # pegando armature
        self.armature = self.object.children.get(args["Armature name:"])
        print(self.armature)

        # pegando velocidades
        self.walkSpeed = args["Walk Speed"]
        self.rotSpeed = args["Rot Speed"]

    def movement(self):
        # movimentando cubo
        keyboard = bge.logic.keyboard.inputs
        speed = self.walkSpeed
        idle = self.idle
        run = self.run
        print(run)
        self.armature.playAction(idle[0], idle[1], idle[2], blendin = 10, priority = idle[3])
        x = 0
        y = 0
        rot = 0
        stop_motion = 0
        if stop_motion == 0:
            if keyboard[bge.events.WKEY].active:
                y = 1
                #self.armature.playAction(run[0], run[1], run[2], blendin = 10, priority = run[3])
            elif keyboard[bge.events.SKEY].active:
                y = -1
            if keyboard[bge.events.EKEY].active:
                x = 1
            elif keyboard[bge.events.QKEY].active:
                x = -1
            if keyboard[bge.events.DKEY].active:
                rot = -1
            elif keyboard[bge.events.AKEY].active:
                rot = 1
        self.object.applyRotation((0, 0, rot/25), True)
        vec = self.object.worldOrientation * Vector([x, y, 0])
        vec.normalize()  
        self.character.walkDirection = vec * speed
    def update(self):# funcao principal
        self.movement()
