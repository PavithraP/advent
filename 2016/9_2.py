
f=open("9.txt","r")
lines=f.readlines()
count = 0
def find(string):
	global count
	c = 0
	while(len(string) != 0):
		token = string.split("(")
		print "token",token
		if(len(token) > 1 and ")" in token[1]):		
			tmp = token[1].split(")")
			t = tmp[0].split("x")
			print string,len(token[0])+len(tmp[0])+1
			v = len(token[0])+len(tmp[0])+2
			print "string",string[v:v+int(t[0])]
			for i in range(int(t[1])):
				print "i=",i,t[1]
				find(string[v:v+int(t[0])])	
				#return int(t[0])+len(token[0])
		else:
			return len(token[0])
			count += len(token[0])
			#l = find(string)
			if( l+5 < len(string)):
				string = string[l+5:]
			else:
				break

	return c+len(token[0])

for line in lines:
	line = line.rstrip().replace(" ","")
	while(len(line) != 0):
		l = find(line)
		if( l+5 < len(line)):
			line = line[l+5:]
		else:
			break
		print count

