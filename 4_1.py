import hashlib
i=0
while True:
	hash1= hashlib.md5("iwrupvqb"+str(i))
	if hash1.hexdigest()[0:5] == "00000":
		break
	i+=1
print i
