import re

countY  = 0
f = open("3.txt","r")
lines = f.readlines()
num = [[0 for i in range(len(lines))] for j in range(3)]
for line in lines:
	line = re.sub(' +',' ',line.rstrip())
	#print line
	countX  = 0
	for n in line.split(" "):
		num[countX][countY] = int(n) 
		countX += 1
	countY += 1
#num[0] = sorted(num[0])
#num[1] = sorted(num[1])
#num[2] = sorted(num[2])
#print num[1]	
i = 0
count = 0
#print "num is ",num[1][
while(i+3 < countY):
	if(((num[0][i] + num[0][i+1]) > num[0][i+2]) and ((num[0][i] + num[0][i+2]) > num[0][i+1]) and ((num[0][i+2] + num[0][i+1]) > num[0][i])):
		count += 1
	i+=3
i = 0
while(i+3 < countY):
	if(((num[1][i] + num[1][i+1]) > num[1][i+2]) and ((num[1][i] + num[1][i+2]) > num[1][i+1]) and ((num[1][i+2] + num[1][i+1]) > num[1][i])):
		count += 1
	i+=3
i = 0
while(i+3 < countY):
	if(((num[2][i] + num[2][i+1]) > num[2][i+2]) and ((num[2][i] + num[2][i+2]) > num[2][i+1]) and ((num[2][i+2] + num[2][i+1]) > num[2][i])):
		count += 1
	i+=3
print count
