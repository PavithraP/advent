import time
t = time.time()
f=open("7.txt","r")
lines=f.readlines()
count  = 0
for line in lines:
	found  = 0
	c = 0
	for i in range(len(line)-3):
		if(line[i] == "["):
			found = 1
		if(line[i] == "]"):
			found = 0
		if(line[i] != line[i+1] and line[i+1] == line[i+2] and line[i] == line[i+3]):
			if(found == 1):
				c = 0
				break
			elif(found == 0):
				c += 1
	if(c > 0):
		count += 1

print count,time.time()-t
