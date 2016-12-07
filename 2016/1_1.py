f = open('1.txt', 'r')
lines = f.readline()
#print lines
up = 1
left = 0
right = 0
down = 0
x = 0
y = 0
for l in lines.rstrip().split(", "):
	if((l[0] == "R" and up == 1)):
		x += int(l[1:])
		right = 1
		up = 0
	elif((l[0] == "L" and up == 1)):
		x -= int(l[1:])
		left  = 1
		up = 0
	elif((l[0] == "R" and right == 1)):
		y -= int(l[1:])
		down = 1
		right  = 0
	elif(l[0] == "L" and right == 1):
		y += int(l[1:])
		up = 1
		right = 0
	elif((l[0] == "L" and left == 1)):
		y -= int(l[1:])
		down = 1
		left = 0
	elif((l[0] == "R" and left == 1)):
		y += int(l[1:])
		up = 1
		left = 0
	elif((l[0] == "L" and down == 1)):
		x += int(l[1:])
		right = 1
		down = 0
	elif((l[0] == "R" and down == 1)):
		x -= int(l[1:])
		left = 1
		down = 0
print abs(x) + abs(y)
