
f=open("9.txt","r")
lines=f.readlines()
count = 0
def find(string,cc):
	global count
	c = 0
	l = 0
	while(len(string) > 0):
		v = 0
		token = string.split("(")
		if(len(token) > 1 and ")" in token[1]):		
			tmp = token[1].split(")")
			t = tmp[0].split("x")
			v = len(token[0])+len(tmp[0])+2
			if len(token[0]) >0 :
				count +=len(token[0])
			find(string[v:v+int(t[0])],int(t[1])*cc)
			string = string[len(token[0])+int(t[0])+len(t[0])+len(t[1])+3:]
		else:
			v = len(token[0])
			find(string[v:],cc)
			string  = string[len(token[0]):]
			count += (len(token[0])*cc)

for line in lines:
	find(line.rstrip(),1)
print count

