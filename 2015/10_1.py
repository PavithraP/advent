num = raw_input("")

no = 0
while( no < 50):
	str1= ""
	i=0
	while(i< len(num)):
		count  = i
		while(  i< len(num)-1 and num[i] == num[i+1]):
			i+=1
		str1+= str(i-count+1)+str(num[count])
		i+=1
	num = str1
	no+=1

print len(str1)

		
	
