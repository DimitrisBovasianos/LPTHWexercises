from sys import exit

def gold_room():
     print "this room is full of gold. how much do you take?"

     choice = raw_input(">")
     if "0" in choice or "1" in choice:
         how_much = int(choice)
     else:
         dead("man,leart to type a number")

     if how_much < 50:
         print "nice, u are not greedy,you win"
         exit(0)
     else:
         dead("u greedy bastard")


def bear_room():
    print "there is a bear here"
    print "the bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "how are u going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take money":
            dead("the bear looks at u then slaps ur face off.")
        elif choice == "taunt bear" and not bear_moved:
            dead("the bear has moved from the door. u can go through now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews ur leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea what that means"


def cthulhu_room():
    print "here u see the great evil cthulhu"
    print "he, it whatever stares at u and u go insane"
    print "do u free for ur life or eats ur head ?"

    choice = raw_input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()


def dead(why):
    print why, "good job"
    exit(0)

def start():
    print "u are in a dark room"
    print "there is a door to ur right and left"
    print "which one do u take?"

    choice = raw_input (">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead ("u stumble around the room until u starve")


start()
