run = [8,17,6,6,12,6,3,4,20]
rest = [165,114,103,145,125,121,50,75,119]
dist = [22,8,18,25,11,21,18,20,7]
tot = [0 for i in range(9)]
mint = [0 for i in range(9)]

flag = 1
count  = 0
sec = 0
while( sec < 2503):
	for i in range(9):
		if ( (sec % (run[i]+rest[i])) < run[i]):
			tot[i] += dist[i]
		
	for i in range(9):
		max1 = max(tot)
		if ( tot[i] == max1):
			mint[i] += 1
	sec += 1 
	

print max(mint)


	
