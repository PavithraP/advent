with open('8_1.txt', 'r') as f:
	lines = f.readlines()

length = 0
for string in lines:
	string = string.replace("\\","$")
	slash = len([i for i in range(len(string)) if string.startswith('$', i)])
	quote = len([i for i in range(len(string)) if string.startswith('"', i)])
	length = length +quote + slash +2

print length

	
