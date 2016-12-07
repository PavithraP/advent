f = open('1.txt', 'r')
lines = f.readline()
#print lines
up = 1
left = 0
right = 0
down = 0
x = 0
y = 0
prev = []
found = 0
for l in lines.rstrip().split(", "):
	if(found == 1):
		break
	if((l[0] == "R" and up == 1)):
		oldX = x+1
		x += int(l[1:])
		right = 1
		up = 0
		for i in range(oldX,x+1):
		#	print str(i)+"."+str(y)
			if(str(i)+"."+str(y) in prev):
				print "found",str(i),str(y)
				found = 1
			else:
				prev.append(str(i)+"."+str(y))
	elif((l[0] == "L" and up == 1)):
		oldX = x-1
		x -= int(l[1:])
		left  = 1
		up = 0
		for i in range(oldX,x-1,-1):
		#	print str(i)+"."+str(y)
			if(str(i)+"."+str(y) in prev):
				print "found",i,y
				found = 1
				break
			else:
				prev.append(str(i)+"."+str(y))
	elif((l[0] == "R" and right == 1)):
		oldY = y-1
		y -= int(l[1:])
		down = 1
		right  = 0
		for i in range(oldY,y-1,-1):
		#	print str(x)+"."+str(i)
			if(str(x)+"."+str(i) in prev):
				print "found",x,i
				found = 1
				break
			else:
				prev.append(str(x)+"."+str(i))
	elif(l[0] == "L" and right == 1):
		oldY = y+1
		y += int(l[1:])
		up = 1
		right = 0
		for i in range(oldY,y+1):
		#	print str(x)+"."+str(i)
			if(str(x)+"."+str(i) in prev):
				print "found",x,i
				found = 1
				break
			else:
				prev.append(str(x)+"."+str(i))
	elif((l[0] == "L" and left == 1)):
		oldY = y-1
		y -= int(l[1:])
		down = 1
		left = 0
#		print "here"
		for i in range(oldY,y-1,-1):
		#	print str(x)+"."+str(i)
			if(str(x)+"."+str(i) in prev):
				print "found",x,i
				found = 1
				break
			else:
				prev.append(str(x)+"."+str(i))
	elif((l[0] == "R" and left == 1)):
		oldY = y+1
		y += int(l[1:])
		up = 1
		left = 0
		for i in range(oldY,y+1):
		#	print str(x)+"."+str(i)
			if(str(x)+"."+str(i) in prev):
				print "found",x,i
				found = 1
				break
			else:
				prev.append(str(x)+"."+str(i))
	elif((l[0] == "L" and down == 1)):
		oldX = x+1
		x += int(l[1:])
		right = 1
		down = 0
		for i in range(oldX,x+1):
		#	print str(i)+"."+str(y)
			if(str(i)+"."+str(y) in prev):
				print "found",i,y
				found = 1
				break
			else:
				prev.append(str(i)+"."+str(y))
	elif((l[0] == "R" and down == 1)):
		oldX = x-1
		x -= int(l[1:])
		left = 1
		down = 0
		for i in range(oldX,x-1,-1):
		#	print str(i)+"."+str(y)
			if(str(i)+"."+str(y) in prev):
				print "found",i,y
				found = 1
				break
			else:
				prev.append(str(i)+"."+str(y))
