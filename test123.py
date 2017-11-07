from sys import argv
script, filename = argv

txt = open(filename)
text = []
for line in txt.readlines():
    text.append(line.strip())
text.sort()
for i in text:
   print i
