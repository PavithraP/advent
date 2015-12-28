import math 
i =1000

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while True:
	fact = factors(i)
	tot = []
	for f in fact:
		if f*50 >= i:
			tot.append(f)
	if sum(tot)*11 >= 33100000:
		break
	i+= 1

print i
