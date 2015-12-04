import hashlib

input = "yzbqklnj"

m = hashlib.md5()
m.update(input)

found = False
count = -1
next = input

while not found:
	count += 1
	next = input + str(count)
	m = hashlib.md5()
	m.update(next)
	if m.hexdigest()[:6] == "000000":
		found = True
		print m.hexdigest()
		print count
