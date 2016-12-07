f = open('2.txt', 'r')
lines = f.readlines()
start = 5
row = 2
for line in lines:
	for l in line.rstrip():
		if(l == "R" and (start < (3*row))):
			start += 1
		elif(l == "L" and (start > (3*(row-1)+1))):
			start -= 1
		elif(l == "U" and (row > 1)):
			row -= 1
			start -= 3
		elif( l == "D" and row < 3):
			row += 1
			start += 3
	print start
