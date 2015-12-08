with open('2_1.txt', 'r') as f:
	lines = f.readlines()
	val = 0
	for line in lines:
		dim = [int(i) for i in line.rstrip().split("x")]
		val += dim[0]*dim[1]*dim[2]
		dim.remove(max(dim))
		val += dim[0]+dim[0]+dim[1]+dim[1]
	print val
			
