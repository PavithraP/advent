with open('8_1.txt', 'r') as f:
	lines = f.readlines()

length = 0
for string in lines:
	#special = sum(not c.isalnum() for c in string)
	string = string.replace("\\\\","$")
	slash = len([i for i in range(len(string)) if string.startswith('$', i)])
	quote = len([i for i in range(len(string)) if string.startswith('"', i)])
	hexc = len([i for i in range(len(string)) if string.startswith('\\x', i)])
#	nothex = len([i for i in range(len(string)) if string.startswith('\\\\x', i)])
#	newhex = len([i for i in range(len(string)) if string.startswith('\\\\\\x', i)])
#	nothsl = len([i for i in range(len(string)) if string.startswith('\\\\\\', i)])
	length = length + (slash + quote + 3*(hexc))
#	string = "\""+string.rstrip()+"\""
#	print string,length, (slash + quote + 3*(hexc-nothex)),nothex
#	print "slash",slash,"quoate",quote,"hexc",hexc
#	print string,length

print length

	
