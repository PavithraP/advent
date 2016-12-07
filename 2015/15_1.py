ing = [[4,-2,0,0],
	[0,5,-1,0],
	[-1,0,5,0],
	[0,0,-2,2]]
max1 = 0

for f in range(100):
	for c in range(100):
		for b in range(100):
			if f+c+b >= 100:
				continue
			s = 100 -(f+c+b)
			cap = f*ing[0][0] + c*ing[1][0] + b*ing[2][0] + s*ing[3][0]
			dur = f*ing[0][1] + c*ing[1][1] + b*ing[2][1] + s*ing[3][1]
			flav = f*ing[0][2] + c*ing[1][2] + b*ing[2][2] + s*ing[3][2]
			text = f*ing[0][3] + c*ing[1][3] + b*ing[2][3] + s*ing[3][3]
			if( cap < 0 or dur < 0 or flav < 0 or text < 0):
				cost = 0
			else: 
				cost = cap * dur * flav * text
			if cost > max1:
				max1 = cost

print max1
