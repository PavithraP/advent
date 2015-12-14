run = [8,17,6,6,12,6,3,4,20]
rest = [165,114,103,145,125,121,50,75,119]
dist = [22,8,18,25,11,21,18,20,7]
tot = [0 for i in range(9)]
tott = [0 for i in range(9)]

flag = 1
for i in range(9):
	while( tott[i] <= 2503):
		if flag == 1:
			if((2503 - tott[i]) < run[i]):
				tot[i] += dist[i]*(2503-tott[i])
			else:			
				tot[i] += dist[i]*run[i]
			tott[i] += run[i]
			flag = 0
		else:
			tott[i] += rest[i]
			flag = 1

print max(tot)


	
