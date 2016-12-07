f = open('2.txt', 'r')
lines = f.readlines()
a = [[-1,-1,1,-1,-1],
     [-1,2,3,4,-1],
     [5,6,7,8,9],
     [-1,'A','B','C',-1],
     [-1,-1,'D',-1,-1]]
row = 2
col = 0
for line in lines:
	for l in line.rstrip():
		if(l == "R" and (col < 4) and a[row][col+1] != -1):
			col += 1
		elif(l == "L" and (col > 0) and a[row][col-1] != -1):
			col -= 1
		elif(l == "U" and (row > 0) and a[row-1][col] != -1):
			row -= 1
		elif( l == "D" and row < 4 and a[row+1][col] != -1):
			row += 1
	print a[row][col]
