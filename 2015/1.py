str1 =raw_input() 
count = 0
pos = 1
for s in str1:
	if s == "(":
		count+=1
	elif s == ")":
		count-=1
	if count == -1:
		print pos
	pos+=1
