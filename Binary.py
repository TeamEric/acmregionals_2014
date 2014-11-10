def num(x):
	if x <2:
		return x
	if x%2==1:
		return x + num(x//2)*2
	if x%2==0:
		return x + num(x//2) + num(x//2-1)

lst = []
x = raw_input()
while x != 0:
	lst.append(x)
	try:
		x = raw_input()

	except:
		x = 0
		pass
cases = []
for a in lst:
	temp = a.split(" ")
	for b in temp:
		try:
			cases.append(int(b))
		except:
			pass
for i in range(0,len(cases)):
	print("Case " + str(i+1)+": " + str(num(cases[i])))