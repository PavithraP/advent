with open('6_1.txt', 'r') as f:
	lines = f.readlines()
l = [[0 for x in range(1000)] for x in range(1000)]
for line in lines:
	words = line.split(" ");
	print words
	if(words[0] == "turn"):
		x = [int(i) for i in  words[2].split(",")]
		y = [int(i) for i in  words[4].split(",")]
		for i in range(x[0],y[0]+1):
			for j in  range(x[1],y[1]+1):
				if( words[1] == "on"):
					l[i][j] += 1
				elif( words[1] == "off"):
					l[i][j] -= 1
					if l[i][j] < 0:
						l[i][j] = 0
	elif(words[0] == "toggle"):
		x = [int(i) for i in  words[1].split(",")]
		y = [int(i) for i in  words[3].split(",")]
		#print x[0],x[1],y[0],y[1]
		for i in range(x[0],y[0]+1):
			for j in  range(x[1],y[1]+1):
				#print i,j
				l[i][j] = l[i][j]+2
count = 0
for i in range(1000):
	for j in  range(1000):
		count+=l[i][j]

print count
			
