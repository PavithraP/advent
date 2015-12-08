with open('5_1.txt', 'r') as f:
	lines = f.readlines()

nice = 0
for line in lines:
	flag2= 0
	flag3= 0	
	other = []
	for i in range(len(line)):
		if(i<len(line)-2 and line[i] == line[i+2]):
			flag2 = 1
		if(i< len(line)-2 and (line[i:i+2] in line[i+2:len(line)])):
				flag3 = 1
			
	if(flag2 == 1 and flag3 == 1):
		nice += 1
print nice 

 
	
