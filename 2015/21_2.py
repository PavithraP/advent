import math
w = [4,5,6,7,8]
wc=[8,10,25,40,74]
a = [1,2,3,4,5,0]
ac = [13,31,53,75,102,0]
rd=[1,2,3,0,0,0]
ra=[0,0,0,1,2,3]
rc = [25,50,100,20,40,80]

maxCost = 0

def play(armor,damage,ring):
	points,playarmor,playdamage  = 100,a[armor],w[damage]
	bossp,bossarmor,bossdamage = 104,1,8
	for r in ring:
		playarmor += ra[r]
		playdamage += rd[r]
	turn  = 1
	while(points > 0 and bossp > 0):
		if turn == 1:
			if (playdamage - bossarmor) < 0:
				bossp -= 1
			else:
				bossp -= (playdamage - bossarmor)
			turn  = 0
		elif turn == 0:
			if(bossdamage - playarmor) < 0:
				points -= 1
			else:
				points -= (bossdamage - playarmor)
			turn = 1
	if bossp > 0:
		cost = wc[damage] + ac[armor] 
		for r in ring:
			cost += rc[r]
		return cost,1
	else:
		return 0,-1
			
for i in range(5):
	for j in range(6):
		for k in range(int(math.pow(2,6))):
			if bin(k).count('1') <= 2:
				armor,damage,count,num = j,i,0,k
				ring = []
				while(num > 0):
					if num%2 == 1:
						ring.append(count)
					count+=1
					num /= 2
			cost,success = play(armor,damage,ring)
			if success == 1 and cost > maxCost:
				maxCost = cost
				
print maxCost
