from sys import exit
from sys import argv
script, filename, filename2 = argv
from random import randint
import random


class setting(object):
    def diff(self):
        print "choose difficulty(easy or hard)"
        difficulty = raw_input(">")
        return difficulty




class opening_scene(object):

    def open(self):
        print """ You just arrived to the tomb.
        Maria your asistant is giving you any new infomration about the tomb.
        You cant believed it..all of your years of work finally paid of..
        You found Tutanahmon tomb with the legendary tressure..
        the opening gate is too small for a big crew..u can only enter you with Maria,
        or sent someone else with her..what will u do ? """
        action = raw_input (">")
        if action == "igo":
             return 'antechamber'
        elif action == "sent someone else":
            print """your crew doesnt like your desicion,the dont want a leader
            that back offs,they all leave and leave u alone there """
            return 'failed'

class Antechamber1(object):

    def open(self):
        print""" you enter the antechamber,u cant see anything...
        you hears bones crushing as you walk..that cant be a good sign..u managed
        to find a torch..fortunatelly maria has a light and finally u light up the room..
        it is magnificent..u look down and u find out that the bones belongs to human skeletons.
        u and maria look each other terrified.."""
        return 'mainchamber'

class Antechamber2(object):

    def open(self):
        print"""you enter the antechamber,u cant see anything...
        you hears bones crushing as you walk..that cant be a good sign..u managed
        to find a torch,but the light is the medical kit Kostas gave u..
        to open the medical kit you need a 4 digit code that kostas yelled at you
        but you only catch 2 of them..which was???"""
        numberuhear = raw_input(">")
        number = "%d%d%d" %(numberuhear, randint(1,5),randint(1,5))
        print """now you have to guess the other,
        keep in mind to put the 2 number u hear first.
        """
        guess = raw_input(">")
        i = 0
        while guess != number and i<9:
            print "try again"
            guess = raw_input(">")
            i += 1
        if guess == number:
                print """ you find it.u took the lighter,
                u lit the torch and you light up the room.
                fortunatelly maria has a light and finally u light up the room..
                it is magnificent..u look down and u find out that the bones belongs to human skeletons.
                u and maria look each other terrified.."""
                return 'mainchamber2'
        else:
            print"""u didnt light up the room..maria was terrified,she start
            running back to the camp and go follow her
            """
            return 'failed'

class Main_chamber(object):


    def open(self):
        print """you and maria enter the main chamber..the room is a 3x3
        square of squares..you must find the correct path..u can only go
        forward,left or right.u stand in the middle square of the first row..
        you only have 5 tries.
        if dont find the correct path,nails will come oute the floor..
        which path will you choose?the square is like this [ ,   , ]
                                                           [ ,   , ]
                                                           [ , Y , ]
        """
        print "a sample is forward,left,right.you have 5 tries"
        samples = open(filename)
        paths = []
        for line in samples.readlines():
            paths.append(line.strip())
        correctpath = random.choice(paths)
        guesspath = raw_input (">")
        i= 0
        while guesspath != correctpath and i<4:
            guesspath = raw_input(">")
            i += 1
        if guesspath == correctpath:
            print "you find the right path you and maria proceed to the last chamber"
            return 'lastchabmer'
        else:
            print "spikes comes out the floor.....the rest is history"
            return 'failed'

class Main_chamber2(object):

    def open(self):
        print """you and maria enter the main chamber..the room is a 4x4
        square of squares..you must find the correct path..u can only go
        forward,left or right.u stand where the Y is..
        you only have 5 tries.
        if dont find the correct path,nails will come oute the floor..
        which path will you choose?the square is like this [ ,  , , ]
                                                           [ ,  , , ]
                                                           [ ,  , , ]
                                                           [ , Y, , ]
        """
        print "a sample is forward,right,forward,left,forward"
        samples2 = open(filename2)
        paths2 = []
        for line in samples2.readlines():
            paths2.append(line.strip())

        correctpath = random.choice(paths2)
        guesspath = raw_input(">")
        i = 0
        while guesspath != correctpath and i<4:
            guesspath = raw_input(">")
            i += 1
        if guesspath == correctpath:
            print "you find the right path you and maria proceed to the last chamber"
            return 'lastchabmer'
        else:
            print "spikes comes out the floor.....the rest is history"
            return 'failed'

class last_chamber(object):


    def open(self):
        print """you finally reached the last chamber,
        you cant believe what you are witnessing..an army of
        skeletons is front a big gate..their leader speaks..
        I SHALL TELL YOU A RIDDLE IF YOU FIND THE correct ANSWER
        TUTANAHAMON TRESSURE IS YOURS..you have 3 tries
        """
        riddles ={
        "There is a certain crime, that if it is attempted, is punishable, but if it is committed, is not punishable. What is the crime?": "suicide",
        "There are four days which start with the letter 'T',tuesday and thursday,name the other two." : "today and tommorow",
        """A boy and his father are caught in a traffic accident, and the father dies.
        Immediately the boy is rushed to a hospital, suffering from injuries.
        But the attending surgeon at the hospital, upon seeing the boy, says
        'I cannot operate. This boy is my son.'

        How is this situation explained ?""" : "she is his mother",
        }
        riddle = random.choice(riddles.keys())
        print riddle
        correctanswer = riddles[riddle]
        guessanswer = raw_input(">")
        i = 0
        while guessanswer != correctanswer and i<2:
            print "guess again.."
            guessanswer = raw_input(">")
            i += 1
        if guessanswer == correctanswer:
            print "you did it..maria hugs you..the door is opening.."
            return 'didit'
        else:
            print "the skeleton killed you"
            return 'failed'

class Didit(object):
    def open(self):
        print"""u finally found the tressure,is magnificent..
        you look at maria,she starts cryning..you hug and kiss her..you tell her
        you want to spent the rest of your life with..she said she wants too.
        that was it..THE end
        """
        return 'didit'

class Failed(object):
    def open(self):
        print """u wasnt able to finish the task..this was a one in a life time
        opportunity...the end """
        exit(1)

class Map1(object):
    scenes = {
    'openingscene' : opening_scene(),
    'antechamber' : Antechamber1(),
    'mainchamber' : Main_chamber(),
    'lastchabmer' : last_chamber(),
    'failed' : Failed(),
    'didit' : Didit(),
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map1.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Map2(object):
    scenes = {
    'openingscene' : opening_scene(),
    'antechamber' : Antechamber2(),
    'mainchamber' : Main_chamber2(),
    'lastchabmer' : last_chamber(),
    'failed' : Failed(),
    'didit' : Didit(),
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map2.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene= self.scene_map.next_scene('didit')

        while current_scene != last_scene:
            next_scene_name = current_scene.open()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.open()

diffic = setting()
scenario = diffic.diff()
if scenario == "easy":
    a_map = Map1('openingscene')
    a_game = Engine(a_map)
    a_game.play()
elif scenario == "hard":
    a_map = Map2('openingscene')
    a_game = Engine(a_map)
    a_game.play()
