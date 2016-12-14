f=open("10.txt","r")
lines=f.readlines()
count = 0
chip={}
low={}
high={}
outputlow={}
outputhigh={}
def parse(c):
	print "c=",c,"chips are",chip[c]
	if(chip[c][0] == "17" and chip[c][1] == "61"):
		print c
	#	return
	else:
		if c in outputlow:
			if outputlow[c] not in chip:
				chip[outputlow[c]] = []
			chip[outputlow[c]].append(chip[c][0])
			chip[outputlow[c]] = sorted(chip[outputlow[c]])
			chip[c].remove(chip[c][0])
			if(len(chip[outputlow[c]]) > 1):
				parse(outputlow[c])
		elif c in low:
			if low[c] not in chip:
				chip[low[c]] = []
			chip[low[c]].append(chip[c][0])
			chip[low[c]] = sorted(chip[low[c]])
			chip[c].remove(chip[c][0])
			if(len(chip[low[c]]) > 1):
				parse(low[c])
		if c in outputhigh:
			if outputhigh[c] not in chip:
				chip[outputhigh[c]] = []
			chip[outputhigh[c]].append(chip[c][0])
			chip[outputhigh[c]] = sorted(chip[outputhigh[c]])
			chip[c].remove(chip[c][0])
			if(len(chip[outputhigh[c]]) > 1):
				parse(outputhigh[c])
		elif c in high:
			if high[c] not in chip:
				chip[high[c]] = []
			chip[high[c]].append(chip[c][0])
			chip[high[c]] = sorted(chip[high[c]])
			chip[c].remove(chip[c][0])
			if(len(chip[high[c]]) > 1):
				parse(high[c])

for line in lines:
	token = line.rstrip().split(" ")
	if(token[0] == "bot"):
		if(token[5] == "output"):
			outputlow[token[1]]=token[6]
		else:
			low[token[1]]=token[6]
		if(token[10] == "output"):
			outputhigh[token[1]]=token[6]
		else:
			high[token[1]]=token[11]
	elif(token[0] == "value"):
		if token[5] not in chip:
			chip[token[5]] = []
		chip[token[5]].append(token[1])
		chip[token[5]] = sorted(chip[token[5]])
		if(len(chip[token[5]]) > 1):
			parse(token[5])
#got = ""
#for c in chip:
#	got = c
#	if(len(chip[c]) > 1):
#		break

#print "got=",got



#parse(got)
#		break
#	print chip[c],c
