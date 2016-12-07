with open('2_1.txt', 'r') as f:
	lines = f.readlines()
	area = 0
	for line in lines:
		minimum = 9999
		dim = line.rstrip().split("x");
		for i in range(3):
			val = int(dim[i])*int(dim[(i+1)%3])
			area += 2*val
			if val < minimum:
				minimum = val
		area += minimum
	print area
			
