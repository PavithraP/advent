import math 
i =1000

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while (sum(factors(i))*10) < 33100000:
	i+= 1

print i
