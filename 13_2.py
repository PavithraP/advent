from random import randint
import math
graph = [[-99,54,-81,-42,89,-89,97,-94,0],
	[3,-99,-70,-31,72,-25,-95,11,0],
	[-83,8,-99,35,10,61,10,29,0],
	[67,25,48,-99,-65,8,84,9,0],
	[-51,-39,84,-98,-99,-20,-6,60,0],
	[51,79,88,33,43,-99,77,-3,0],
	[-14,-12,-52,14,-62,-18,-99,-17,0],
	[-36,76,-34,37,40,18,7,-99,0],
	[0,0,0,0,0,0,0,0,-99]]

noOfParticles = 20
noOfCities = 9
particle=[[] for i in range(noOfParticles)]
def initiateParticles():
	i = 0
	while i < noOfParticles:
		temp_graph = [[0,54,-81,-42,89,-89,97,-94,0],
			[3,0,-70,-31,72,-25,-95,11,0],
			[-83,8,0,35,10,61,10,29,0],
			[67,25,48,0,-65,8,84,9,0],
			[-51,-39,84,-98,0,-20,-6,60,0],
			[51,79,88,33,43,0,77,-3,0],
			[-14,-12,-52,14,-62,-18,0,-17,0],
			[-36,76,-34,37,40,18,7,0,0],
			[0,0,0,0,0,0,0,0,0]]
		count = 0
		no = randint(0,8)
		temp = no
		particle[i]=[]
		particle[i].append(no)
		while count < noOfCities-1:
			no = randint(0,8)
			if no not in particle[i] and graph[temp][no]!= -1 and graph[temp][no]!= -99:
				for k in range(noOfCities):
					temp_graph[temp][k] = 0
					temp_graph[k][temp] = 0 
				particle[i].append(no)
				temp = no
				count += 1
			elif temp_graph[temp].count(0)+temp_graph[temp].count(-1) == noOfCities:
				i -= 1
				break;
		i += 1

def costCalculation(particle):
	cost = 0
	for i in range(noOfCities):
		cost += graph[particle[i]][particle[(i+1)%noOfCities]] + graph[particle[(i+1)%noOfCities]][particle[(i)]]
	return cost

def check(part, source ,dest):
	source = int(source)%noOfCities
	dest = int(round(dest,0))%noOfCities
	if source > dest:
		tmp = source
		source = dest
		dest = tmp
	elif source == dest:
		return 0
	if graph[part[dest]][part[source+1]] != -1 :
		if graph[part[source]][part[dest-1]] != -1 :
			if source-1 < 0:
				if dest+1 >= noOfCities:
					return 1
				elif graph[part[source]][part[dest+1]] != -1 :
					return 1
				else:
					return 0	
			elif graph[part[dest]][part[source-1]] != -1:
				if dest+1 >= noOfCities:
					return 1
				elif graph[part[source]][part[dest+1]] != -1 :
					return 1
				else:
					return 0	
			else:
				return 0	
	else:
		return 0	
				  	
def swap(part, source ,dest):
	source = int(source)%noOfCities
	dest = int(round(dest,0))%noOfCities
	#print "part=",part,source,dest
	tmp = part[source]
	part[source] = part[dest]
	part[dest] = tmp
	return part

pRandom = 0.9
pPbest = 0.05
pGbest = 0.05
pBest = [0.0 for i in range(noOfParticles)]
v = [1 for i in range(noOfParticles)]
gBest = 0.0

initiateParticles()
print particle 

for i in range(noOfParticles):
	present = costCalculation(particle[i])
	if present > pBest[i]:
		pBest[i] = present
	if present > gBest:
		gBest = present
iterations = 1000
change = 0
flag = 0

while( iterations > 0):
	merged = 0
	for i in range(noOfParticles):
		cost = costCalculation(particle[i])
		print "before change =",particle[i],"cost =",pBest[i]
		prevV = v[i]
		v[i] = pRandom * v[i] + pPbest * (pBest[i] - cost) + pGbest * (gBest - cost)
		isSwappable = check(particle[i],prevV,(prevV+v[i]))
		if isSwappable == 1:
			temp_part = swap(particle[i],prevV,(prevV+v[i]))
			cost = costCalculation( temp_part )
			if cost > pBest[i]:
				particle[i] = temp_part
				pBest[i] = cost
				print "after change =",particle[i],"cost =",cost
				change += 1
			if cost > gBest:
				gBest = cost
		if gBest == pBest[i]:
			merged += 1
		print "\n"
		
	print "merged",merged
	if merged > noOfParticles / 2:
		iterations = 0
	pRandom *= 0.95
	pPbest *= 1.01
	pGbest = 1 - (pRandom + pPbest) 
	flag += 1
	print "change***************",change

print change
print "flag =",flag
