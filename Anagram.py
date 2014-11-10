
def inWord(a,b):
	la = []
	lb = []
	for i in a:
		la.append(i)
	for i in b:
		lb.append(i)
	a = la
	b = lb
	a.sort()
	b.sort()
	diff = 0
	for i in range(0,len(b)):
		if a[i+diff]!=b[i]:
			if  diff == 1:
				return False
			diff+=1
	return True
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
		if len(b)>0:
			try:
				cases.append(int(b))
			except:
				cases.append(b)
x = 0
casen = 1
while x <len(cases):
	eggs = dict()
	leng = 0
	for i in range(0,cases[x]):
		ins = cases[x+i+1].upper()
		if len(ins) in  eggs:
			eggs[len(ins)][ins]=[ins]
		else:
			eggs[len(ins)]=dict()
			eggs[len(ins)][ins]=[ins]
		if len(ins)>leng:
			leng = len(ins)

	cases2 = []
	x+=cases[x]+1
	for i in range(0,cases[x]):
		cases2.append(str(cases[x+i*2+1])+" "+str(cases[x+i*2+2]))
	x+=cases[x]*2+1
	while leng>0:
		if leng in eggs and (leng-1) in eggs:
			for a in eggs[leng]:
				for b in eggs[leng-1]:
					if inWord(a,b):
						for j in eggs[leng][a]:
							eggs[leng-1][b].append(j)

		leng-=1
	print("Case "+str(casen)+":")
	casen+=1
	for case in cases2:
		case = case.split(" ")
		try:
			case1 = case[0]
			case2 = case[1]
			case1 = case1.upper()
			case2 = case2.upper()
			eggs[len(case1)][case1].index(case2)
			print("yes")
		except:
			print("no")