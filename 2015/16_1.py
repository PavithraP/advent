with open('16.txt', 'r') as f:
	lines = f.readlines()
	
dic = {'children':3 , 'cats':7 ,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}
aunt = 0
for line in lines:
	val = line.rstrip().split(',')
	flag = 1
	count = 0
	for v in val:	
		x = v.split(':')
		if flag == 1:
			x[1] = x[1].replace(" ", "")
			x[2] = x[2].replace(" ", "")
			if dic[x[1]] == int(x[2]):
				count+=1
			flag = 0
		else:
			x[0] = x[0].replace(" ", "")
			x[1] = x[1].replace(" ", "")
			if dic[x[0]] == int(x[1]):
				count+=1
	aunt += 1
	if count == len(val):
		print aunt
