
f=open("tmp","r")
lines=f.readlines()
count = 0
def find(string,cc):
	global count
	print string,count
	c = 0
	l = 0
	#print len(string)
#	string = string.rstrip()
	while(len(string) > 0):
		v = 0
		token = string.split("(")
		#print "token",token,count,string
		#print token[0]
		if(len(token) > 1 and ")" in token[1]):		
			tmp = token[1].split(")")
			t = tmp[0].split("x")
			v = len(token[0])+len(tmp[0])+2
			print "******",token
			if len(token[0]) >0 :
				count +=len(token[0])
			#for i in range(int(t[1])):
				#print "i = ",i,t[1]
			find(string[v:v+int(t[0])],int(t[1])*cc)
			#print string,"toekn",token[0],"t",t[0]
			string = string[len(token[0])+int(t[0])+len(t[0])+len(t[1])+3:]
			#print "string=",string
		else:
			v = len(token[0])
			find(string[v:],cc)
		#	return
	#	print "******",string,l,token[0]
			string  = string[len(token[0]):]
			#print "*******",token[0]
			count += (len(token[0])*cc)
	#	print "End",string

for line in lines:
	find(line.rstrip(),1)
print count

