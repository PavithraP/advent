import operator
f=open("7.txt","r")
lines=f.readlines()
count  = 0
for line in lines:
	found  = 0
	tmp = []
	res = []
	for i in range(len(line)-2):
		if(line[i] == "["):
			found = 1
		if(line[i] == "]"):
			found = 0
		if(line[i] != line[i+1] and line[i] == line[i+2]):
			if(found == 1):
				tmp.append(line[i]+line[i+1]+line[i])
			elif(found == 0):
				res.append(line[i+1]+line[i]+line[i+1])
	for t in tmp:
		if t in res:
			count += 1
			break
				

print count
