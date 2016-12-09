
f=open("9.txt","r")
lines=f.readlines()
count = 0
def find(string):
	global count
	token = line.split("(")
	if(len(token) > 1 and ")" in token[1]):		
		t = token[1].split(")")[0].split("x")
		count += (int(t[0]) * (int(t[1])))
		return (int(t[0])+len(token[0]))
	count += len(token[0])
	return len(token[0])

for line in lines:
	line = line.rstrip().replace(" ","")
	while(len(line) != 0):
		l = find(line)
		if( l+5 < len(line)):
			line = line[l+5:]
		else:
			break
		print count

