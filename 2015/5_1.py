with open('5_1.txt', 'r') as f:
	lines = f.readlines()

vow = "aeiou"
other = ["ab","cd","pq","xy"]
nice = 0
for line in lines:
	flag1 = 0 
	flag2= 0
	flag3= 0	
	#print line,
	for i in range(len(line)):
		if(line[i] in vow):
			flag1 += 1
		if(i!= len(line)-1 and line[i] == line[i+1]):
			flag2 = 1
		if(i!= len(line)-1 and (line[i:i+2] in other)):
			flag3 = 1
			
	if(flag1 >= 3 and flag2 == 1 and flag3 == 0):
		nice += 1
	#	print " nice"
print nice 

 
	
