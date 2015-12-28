lights = [[0 for i in range(100)] for j in range(100)]
temp = [[0 for i in range(100)] for j in range(100)]


with open('18.txt', 'r') as f:
	lines = f.readlines()

count = 0
for line in lines:
	for i in range(100):
		if line[i] == '#':
			lights[count][i] = 1
		elif line[i] == ".":
			lights[count][i] = 0
	count += 1
#print lights
k=0
while(k< 100):
	for i in range(100):
		for j in range(100):
			count = 0
			#print i,j,lights[i][j]
			if(j>0 and lights[i][j-1] == 1):
				count +=1	
			if(j<99 and lights[i][j+1] == 1):
				count +=1	
			if(i<99 and lights[i+1][j] == 1):
				count +=1	
			if(i> 0 and lights[i-1][j] == 1):
				count +=1	
			if(i<99 and j< 99 and lights[i+1][j+1] == 1):
				count +=1	
			if(i<99 and j>0 and lights[i+1][j-1] == 1):
				count +=1	
			if(i>0 and j>0 and lights[i-1][j-1] == 1):
				count +=1	
			if(i>0 and j<99 and lights[i-1][j+1] == 1):
				count +=1
			#print count
			#raw_input("")
			if (lights[i][j] == 1):
				if (count == 2 or count == 3):	
					temp[i][j] = 1
				else:
					temp[i][j]= 0
			if(lights[i][j] == 0):
				if (count == 3):
					temp[i][j] = 1
				else:
					temp[i][j] = 0
	for i in range(100):
		for j in range(100):
			lights[i][j] = temp[i][j]
	k+=1

count = 0
for i in range(100):
	for j in range(100):
		if lights[i][j] == 1:
			count+=1
print count
