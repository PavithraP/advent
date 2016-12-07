with open('3_1.txt', 'r') as f:
	lines = f.readlines()
#	print "inout is ",len(lines)
house = 1
c = dict()
c[str(0)] =[]
c[str(0)].append(str(0))
def fun(i):
	hcout = 0
	vcount = 0
	alt = 1
	global house,c
	for line in lines:
		for s in line:
			if alt == i:
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
			alt = (alt+1)%2
fun(0)
fun(1) 
print house


