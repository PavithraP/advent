with open('7_1.txt', 'r') as f:
	lines = f.readlines()
	
op = dict()
for line in lines:
	word = line.rstrip().split("->")
	op[word[1].rstrip().split()[0]] = word[0].rstrip()
op["b"] = "956"

def fn(val):
	global op
	word = op[val].split(" ")
	if val.isdigit():
		return int(val)
	elif op[val].isdigit():
		return int(op[val])
	if len(word) == 3:
		op1 = -999
		op2 = -999
		if not word[0].isdigit() and not op[word[0]].isdigit():
			op1 = fn(word[0])
		elif word[0].isdigit():
			op1 = int(word[0])
		elif op[word[0]].isdigit():
			op1 = int(op[word[0]])
		
		if not word[2].isdigit() and not op[word[2]].isdigit():
			op2 = fn(word[2])
		elif word[2].isdigit():
			op2 = int(word[2])
		elif op[word[2]].isdigit():
			op2 = int(op[word[2]])
		if op1 != -999 and op2 != -999:
			if word[1] == "AND":
				op[val] = str(op1 & op2)
				return  op1 & op2
			elif word[1] == "OR":
				op[val] = str(op1 | op2)
                                return op1 | op2
			elif word[1] == "LSHIFT":
				op[val] = str(op1 << op2)
                                return op1 << op2
			elif word[1] == "RSHIFT":
				op[val] = str(op1 >> op2)
                                return op1 >> op2
	elif len(word) == 2:
		if word[1].isdigit():
			cal = ~int(word[1])
			op[val] = str(cal)
			return ~int(word[1])
		elif op[word[1]].isdigit():
			cal = ~int(op[word[1]])
			op[val] = str(cal)
			return ~int(op[word[1]])
		else:
			op[val] = str( ~ fn(word[1]))
			return ~fn(word[1])
	elif len(word) == 1:
		if word[0].isdigit() or word[0][0] == '-':
			op[val] = str(int(word[0]))
			return int(word[0])
		elif op[word[0]].isdigit():
			op[val] = str(int(op[word[0]]))
			return int(op[word[0]])
		
		else:
			op[val] = str(fn(word[0]))
			return fn(word[0])
print fn("a")
