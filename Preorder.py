def trav(x):
	if x==0:
		return []
	ans = [x[0]]

	temp = trav(x[1])
	for a in temp:
		ans.append(a)
	temp = trav(x[2])
	for a in temp:
		ans.append(a)
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
actcases = [[]]
j = 0
for a in cases:
	if a>0:
		actcases[j].append(a)
	else:
		j+=1
		actcases.append([])
casn = 1
for b in actcases:
	if len(b)==0:
		break
	pancakes = [b[0],0,0]
	for i in range(1,len(b)):
		temp = pancakes
		while True:
			if temp[0]<b[i]:
				if temp[2]==0:
					temp[2]=[b[i],0,0]
					break
				else:
					temp = temp[2]
			elif temp[0]>b[i]:
				if temp[1]==0:
					temp[1]=[b[i],0,0]
					break
				else:
					temp = temp[1]
			else:
				break
	t = trav(pancakes)
	if len(b)!=len(t):
		print("Case " + str(casn) + ": " + "no")
		casn+=1
		continue
	done = True
	for i in range(0,len(b)):
		if b[i]!=t[i]:
			print("Case " + str(casn) + ": " + "no")
			casn+=1
			done = False
			break
	if done==False:
		continue
			
	print("Case " + str(casn) + ": " + "yes")
	casn+=1
	continue