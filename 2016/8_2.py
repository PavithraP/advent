
f=open("8.txt","r")
lines=f.readlines()
x = 50
y = 6
a=[[" " for i in range(x)]for j in range(y)]
#print a
for line in lines:
	#print line 
	token = line.rstrip().split(" ")
	if token[0] == "rect":
		t = token[1].split("x")
		for i in range(int(t[1])):
			for j in range(int(t[0])):
				a[i][j] = "#"
	elif token[0] == "rotate":
		t = token[2].split("=")
		if token[1] == "row":
			b = []
			for i in range(x):
				b.append(a[int(t[1])][i])
			for i in range(x):
				a[int(t[1])][(i+int(token[4]))%x] = b[i]
		elif token[1] == "column":
			b = []
			for i in range(y):
				b.append(a[i][int(t[1])])
			for i in range(y):
				a[(i+int(token[4]))%y][int(t[1])] = b[i]

for i in range(y):
	for j in range(x):
		print a[i][j],
	print
print

