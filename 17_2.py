import math

cont = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3]
no = 0
minc = 1000
for i in range(int(math.pow(2,20))):
	num = i
	count = 0
	val = 0
	noCont = 0
	while(num > 0):
		if num%2 == 1:
			val += cont[count]
			noCont += 1
		num = num / 2
		count += 1
	if val == 150 and noCont < minc:
		minc = noCont
		no = 1
	if val == 150 and noCont == minc:
		no+= 1
print no-1
	
