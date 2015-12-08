with open('3_1.txt', 'r') as f:
	lines = f.readlines()
#	print "inout is ",len(lines)
house = 1
c = dict()
hcout = 0
vcount = 0
c[str(0)] =[]
c[str(0)].append(str(0))
for line in lines:
	for s in line:
		if s == '^':
			hcout += 1
		elif s == 'v':
			hcout -= 1
		elif s == '<':
			vcount -= 1
		elif s == '>':
			vcount += 1
		if not str(hcout) in c:
			c[str(hcout)] = []
			c[str(hcout)].append(str(vcount))
			house += 1
		else:
			if str(vcount) not in c[str(hcout)]:
				c[str(hcout)].append(str(vcount))
				house += 1
print house


