import re
with open('12.txt', 'r') as f:
	lines = f.read()

r = re.compile(r'(-*[\d]*)')
results = r.findall(lines)
sum1 = 0
for x in results:
	if(x.isdigit() or (len(x)>1 and x[0] == '-')):
		sum1 += int(x)
		print int(x)
print sum1
