from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene :
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):
    quips = [
        "you died.sucker..",
        "your dad is not proud fool",
        "such a waste of time",
        "u died like a little bitch"
    ]

    def enter(self):
        print Death.quips[randint(0,len(Death.quips)-1)]
        exit(1)

class CentralCorridor(Scene):


    def enter(self):
        print """ the gothons of planet percal #25 have invade ur ship and killed all
        of ur men..u are the only one left.ur mission is to take a bomb from the armory,placed it to the brigde,escape and blow them to pieces.
        a gothon aproaches..what will u do ? """
        action = raw_input(">")
        if action == "shoot" :
            return 'death'
        elif action == "run" :
            return 'death'
        elif action == "tell a joke" :
            return 'laser_weapon_armory'
        else :
            print "really?ur answer is incorrect"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

        def enter(self):
            print "you try enter the weapon armory but there is a keypad.u must find the correct password.you have 10 tries"
            code = "%d%d%d" %(randint(1,5) , randint (1,5) , randint (1,5))
            attempt = raw_input("keyboard")
            tries = 0
            while attempt != code and tries < 10 :
                print "try again"
                attempt = raw_input()
                tries += 1
            if attempt == code :
                print """ crab the bomb and start running to the brigde"""
                return 'the_brigde'
            else :
                print "the gothons find and splits ur guts out"
                return 'death'

class TheBridge(Scene):

    def enter(self):
        print """ u reached the brigde.. there is a gothon,
        u have to pass it in order to place the bomb..what will u do???
        """
        action = raw_input (">")
        if action == "shoot the gothon":
            return 'death'
        elif action == "throw away the bomb and run":
            return 'death'
        elif action == "tell a joke ":
            print "the joke worked and u avoid the gothon"
            return 'escape_pod'
        else:
            print "wrong again..the gothon killed u"
            return 'death'

class EscapePod(Scene):

    def enter(self):
        print """ u placed the bomb and now u must find the right pod to escape
        there are 5 pods.which one will u choose? """
        good_pod = randint(1,5)
        guess = raw_input ("which one ?")
        if int(guess) != good_pod:
            print "wrong pod.."
            return 'death'
        else:
            print "u find the right one..u done it"
            return 'finished'

class Finished(Scene):
    def enter(self):
        print "u won the game,well done "
        return 'finished'




class Map(object):
    scenes = {
    'central_corridor' : CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_brigde':TheBridge(),
    'EscapePod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
