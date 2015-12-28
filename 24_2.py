import itertools

comb=[[] for i in range(14)]
w = [1,3,5,11,13,17,19,23,29,31,37,41,43,47,53,59,67,71,73,79,83,89,97,101,103,107,109,113]
total = sum(w)/4
list1=[]
length = {}
for i in range(3,14):
	comb[i] = itertools.combinations(range(28), i)


for i in range(3,14):
	for x in comb[i]:
		we = 0
		for k in x:
			we += w[k]
		if we == total:
			list1.append(x)
for l in list1:
	if len(l) not in length:
		length[len(l)] = []
	length[len(l)].append(l)

print "here",len(list1)
#print length[6]
#for i in range(3,11):
#	comb[i] = itertools.combinations(range(28), i)
got  = 0
minw = 999999999999999999999
for i in range(len(list1)):
	first = list1[i]
	print "***********",i,len(list1[i])
	for j in range(i+1,len(list1)):
		second = list1[j]
		if len(set(second).intersection(first)) != 0:
				continue
		for k in range(j+1,len(list1)):
			third = list1[k]
			if len(set(second).intersection(third)) != 0 or len(set(third).intersection(first)) != 0:
					continue
			if (len(first)+len(second)+len(third) >= 28) or (28-(len(first)+len(second)+len(third)) not in length):
				continue
			for forth in length[28-(len(first)+len(second)+len(third))]:				
				if len(set(second).intersection(forth)) != 0 or len(set(third).intersection(forth)) != 0 or len(set(first).intersection(forth)) != 0 :
					continue
				we = 1
				print "got",second,first,third,forth
				for x in first:
					we *= w[x]
				print "we",we
				if we < minw:
					minw = we
					print "minimu is ",minw
					exit()
		
		
