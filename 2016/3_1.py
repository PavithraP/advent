import re
f = open("3.txt","r")
lines = f.readlines()
count  = 0
for line in lines:
	line = re.sub(' +',' ',line.rstrip())
	num = [int(n) for n in line.split(" ")]
	num = sorted(num)
	if((num[0]+num[1]) > num[2]):
		count += 1
print count
