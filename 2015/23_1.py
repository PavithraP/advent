with open('23.txt', 'r') as f:
	lines = f.readlines()

reg = [0,0]
i = 0
while (i< len(lines) and i>=0):
	words = lines[i].rstrip().split(" ")
	print words,i,reg
	if len(words) == 2:
		if words[0] == "hlf":
			reg[ord(words[1])-97]/= 2
		elif words[0] == "tpl":
			reg[ord(words[1])-97] *= 3
		elif words[0] == "inc":
			reg[ord(words[1])-97] += 1
		elif words[0] == "jmp":
			if words[1][0] == '+':
				x = words[1].split('+')
				i =i+ int(x[1])-1
			elif words[1][0] == '-':
				x = words[1].split('-')
				i = i - int(x[1])-1
	elif len(words) == 3:
		if words[0] == "jie":
			if(reg[ord(words[1][0])-97] % 2 == 0):	
				if words[2][0] == '+':
					x = words[2].split('+')
					i =i+ int(x[1])-1
				elif words[2][0] == '-':
					x = words[2].split('-')
					i =i- int(x[1])-1
		elif words[0] == "jio":
			if(reg[ord(words[1][0])-97] == 1):	
				if words[2][0] == '+':
					x = words[2].split('+')
					i =i+ int(x[1])-1
				elif words[2][0] == '-':
					x = words[2].split('-')
					i =i-int(x[1])-1
	i+=1
print reg
