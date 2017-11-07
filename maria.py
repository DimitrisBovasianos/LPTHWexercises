from sys import argv
script, filename = argv
txt = open(filename)
text = []
for line in txt.readlines():
    text.append(line.strip())
mam = len(text)
print mam
points = 0
i = 0
while i < len(text):
    if "i" in text[i]:
        points = points + 1
        i = i + 1
    else:
        i = i + 1
print points
