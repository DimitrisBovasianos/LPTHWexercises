def loop(i, numbers, top):

    while i < top:
        print "the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "numbers now:", numbers
        print "at the bottom  i is %d" % i
        if i == 6:
            return numbers
numbers = loop(0, [], 6)
print len(numbers)
for i in numbers:
    print i
