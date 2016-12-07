import operator
f=open("6.txt","r")
lines=f.readlines()
i = 0
while(i<8):
	m = {}
	for line in lines:
		if line[i] in m:
			m[line[i]] += 1
		else:
			m[line[i]] = 0
	sorted_x = sorted(m.items(), key=operator.itemgetter(1),reverse=True)
	print sorted_x[0][0],
	i += 1

