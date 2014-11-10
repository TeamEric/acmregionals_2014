def BaconSort(x):
	if len(x)==1:
		return x
	elif len(x)==0:
		return []
	ans = []
	x1 = BaconSort(x[:len(x)//2:])
	x2 = BaconSort(x[len(x)//2::])
	i = 0
	j = 0
	while i<len(x1) or j<len(x2):
		if i>=len(x1):
			ans.append(x2[j])
			j+=1
		elif j>=len(x2):
			ans.append(x1[i])
			i+=1
		else:
			if x1[i][0]<x2[j][0]:
				ans.append(x1[i])
				i+=1
			else:
				ans.append(x2[j])
				j+=1
	return ans
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
casen = 1
x = 0
while x <len(cases):
	t = cases[x]
	x+=1
	j1 = []
	j2 = []
	for i in range(0,t):
		j1.append([cases[x+i],i])
		j2.append([cases[x+i+t],i])
	j1 = BaconSort(j1)
	j2 = BaconSort(j2)
	x+=2*t
	Agree = True
	for i in range(0,t):
		if j1[t-i-1][1]!=j2[t-i-1][1]:
			Agree = False
			print("Case " + str(casen) + ": " + str(i+1))
			break
	if Agree:
		print("Case " + str(casen) + ": agree")
	casen+=1
	