import random

s = ["Magic","Drain","Shield","Poison","Recharge"]
maxcost = 9999

def play(spell,total,bossp,points,mana,armor,sh,p,r):
	global s,maxcost 
	if total > maxcost:
		return
	points -= 1
	if points <= 0:
		return 
	if(sh > 0):
		armor = 7
		sh -= 1
	if(p > 0):
		bossp -= 3
		p -= 1
	if(r > 0):
		mana += 101
		r -= 1
	if(sh > 0 and spell == s[2]):
		return 
	if(p > 0 and spell == s[3]):
		return
	if(r > 0 and spell == s[4]):
		return
	if bossp <= 0:
		if total < maxcost:
			maxcost = total
		print "total**********",maxcost
		return 

	if spell == s[0]:
		mana -= 53
		total += 53
		bossp -= 4
	elif spell == s[1]:
		mana -= 73
		total += 73
		bossp -= 2
		points += 2
	elif spell == s[2]:
	#	if(sh > 0):
	#		return
		mana -= 113
		total += 113
		sh = 6
	elif spell == s[3]:
	#	if(p > 0):
	#		return
		mana -= 173
		total += 173
		p = 6
	elif spell == s[4]:
	#	if(r > 0):
	#		return
		mana -= 229
		total += 229
		r = 5
	if mana < 0:
		return
	if bossp <= 0 and mana >= 0:
		if total < maxcost:
			maxcost = total
		print "total**********",maxcost
		return 
	armor = 0
	if(sh > 0):
		armor = 7
		sh -= 1
	if(p > 0):
		bossp -= 3
		p -= 1
	if(r > 0):
		mana += 101
		r -= 1
	
	if bossp <= 0:
		if total < maxcost:
			maxcost = total
		print "total**********",maxcost
		return 
	#if armor>=10:
	#	armor = 9
	points = points - (10-armor)
	armor = 0
	#print "after boss ",spell,bossp,points,sh,p,r,total
	#raw_input("")
	if points <= 0:
		return 
	for i in range(5):
		play(s[i],total,bossp,points,mana,armor,sh,p,r)
	return


for i in range(5):
	print "***************"
	#raw_input("")
	play(s[i],0,71,50,500,0,0,0,0) 

print maxcost
	
