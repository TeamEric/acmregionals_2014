def ncr(n,r):
	ans = 1
	for i in range(r+1,n+1):
		ans*=i
	for j in  range(2,n-r+1):
		ans = ans/j
	return ans
x = raw_input()
def recur(i,lst,s,toSum):
	if s==0:
		if toSum:
			return 1
		else:
			return 0
	if i>=len(lst)-1:
		if toSum:
			return s+1
		else:
			return s
	
	su = 0
	for j in range(0,s+1):
		su+=recur(i+1,lst,s-j,toSum and j<=lst[i])
		if i==0:
			print(j,su)
	return su

casen = 1
while x != "0":
	x = x.split(" ")
	lst = []
	for i in range(1,len(x)):
		lst.append(int(x[i]))
	#ans = recur(0,lst,sum(lst),True)
	ans = 0
	ans = ncr(len(lst)+sum(lst)-1,sum(lst)-1)
	st = 0
	for i in range(0,len(lst)-1):
		for j in range(0,lst[i]):
			ans+=ncr(len(lst)-i-1+sum(lst)-st-j-1,sum(lst)-j-st)
		st+=lst[i]
	ans+=1
	print("Case " + str(casen) + ": " + str(ans))
	x = 0
	try:
		x = raw_input()
	except:
		x = "0"
		pass