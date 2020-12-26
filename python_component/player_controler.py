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
        ("Anime run priorit:", 0), 
        ("Anime bak name:", ""), 
        ("Anime bak S_frame:", 0), 
        ("Anime bak E_frame:", 0), 
        ("Anime bak priorit:", 0), 
        ("Anime turn name:", ""), 
        ("Anime turn S_frame:", 0), 
        ("Anime turn E_frame:", 0), 
        ("Anime turn priorit:", 0), 
        ("Anime runL name:", ""), 
        ("Anime runL S_frame:", 0), 
        ("Anime runL E_frame:", 0), 
        ("Anime runL priorit:", 0), 
        ("Anime runR name:", ""), 
        ("Anime runR S_frame:", 0), 
        ("Anime runR E_frame:", 0), 
        ("Anime runR priorit:", 0), 
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

        self.bak = (args["Anime bak name:"], 
        args["Anime bak S_frame:"], 
        args["Anime bak E_frame:"], 
        args["Anime bak priorit:"])

        self.turn = (args["Anime turn name:"], 
        args["Anime turn S_frame:"], 
        args["Anime turn E_frame:"], 
        args["Anime turn priorit:"])

        self.runL = (args["Anime runL name:"], 
        args["Anime runL S_frame:"], 
        args["Anime runL E_frame:"], 
        args["Anime runL priorit:"])

        self.runR = (args["Anime runR name:"], 
        args["Anime runR S_frame:"], 
        args["Anime runR E_frame:"], 
        args["Anime runR priorit:"])

        self.character = bge.constraints.getCharacter(self.object)
        
        self.armature = self.object.children.get(args["Armature name:"])
        
        self.walkSpeed = args["Walk Speed"]
        self.rotSpeed = args["Rot Speed"]

    def movement(self):
        keyboard = bge.logic.keyboard.inputs
        speed = self.walkSpeed
        idle = self.idle
        run = self.run
        bak = self.bak
        turn = self.turn
        runL = self.runL
        runR = self.runR
        x = 0
        y = 0
        rot = 0
        stop_motion = 0
        if stop_motion == 0:
            control = 0
            if keyboard[bge.events.WKEY].active:
                control = 1
                y = 1
                self.armature.playAction(run[0], run[1], run[2], blendin = 10, play_mode = 0, priority = run[3])
            
            elif keyboard[bge.events.SKEY].active:
                control = 1
                y = -1
                self.armature.playAction(bak[0], bak[1], bak[2], blendin = 10, play_mode = 0, priority = bak[3])
            if keyboard[bge.events.EKEY].active:
                control = 1
                x = 1
            elif keyboard[bge.events.QKEY].active:
                control = 1
                x = -1
            if keyboard[bge.events.DKEY].active:
                control = 1
                rot = -1
                self.armature.playAction(turn[0], turn[1], turn[2], blendin = 10, play_mode = 0, priority = turn[3])
            elif keyboard[bge.events.AKEY].active:
                control = 1
                rot = 1
                self.armature.playAction(turn[0], turn[1], turn[2], blendin = 10, play_mode = 0, priority = turn[3])
            if control == 0:
                self.armature.playAction(idle[0], idle[1], idle[2], blendin = 10, priority = idle[3])

        self.object.applyRotation((0, 0, rot/25), True)
        vec = self.object.worldOrientation * Vector([x, y, 0])
        vec.normalize()  
        self.character.walkDirection = vec * speed
    def update(self):# funcao principal
        self.movement()
