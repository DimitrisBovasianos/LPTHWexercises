print "you enter a dark room with two doors.do you go through door #1 or door #2??"

door = raw_input(">")

if door == "1":
    print "there is a giant bear eating a cheese cake.what do u do?"
    print "1 .take the cake"
    print "2. scream at the bear."

    bear = raw_input(">")

    if bear == "1":
        print "the bear eats ur face good job"
    elif bear == "2":
        print "the bear eats ur legs off good job"
    else:
        print "well, doing %s is probably better.the bear run away" % bear

elif door =="2":
    print "u stare into the endless abyss at cthulhu's retina"
    print "1. blueberries"
    print "2. yellow jacket clothenspins"
    print "3. understanding revolvers yelling melodies"

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "ur body survives powered by a mind of jello.good job"
    else:
        print "the insanity rots ur eyes into the pool of muck.good job"
else:
    print "u stable into a knife and killed urself"
    
