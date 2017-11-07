
states = {
'oregon': 'or',
'florida': 'fl',
'california': 'ca',
'new york': 'ny',
'michigan': 'mi'
}


cities = {
'ca': 'san fransisco',
'mi': 'detroit',
'fl': 'jacksonville'
}


cities['ny'] = 'new york'
cities['or'] = 'portland'


print '-' * 10
print "ny state has: ", cities[ 'ny']
print "or state has: ",cities['or']


print '-' * 10
print "michigan's abberviation is: ", states ['michigan']
print "florida's abberviation is: ", states ['florida']


print '-' * 10
print "michigan has: ", cities[states['michigan']]
print "florida has: ", cities[states['florida']]


print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)


print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)


    print '-' * 10
    for state,abbrev in states.items():
        print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])


print '-' * 10

state = states.get('texas')

if not state:
    print "sorry, no texas"


city = cities.get('tx','does not exist')
print "the city for the state 'tx' is: %s" % city
