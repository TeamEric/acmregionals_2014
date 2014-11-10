x = raw_input()
def ncr(n,r):
	ans = 1
	for i in range(r+1,n+1):
		ans*=i
	for j in  range(2,n-r+1):
		ans = ans/j
	return ans
def better(n,r):
	if r==1:
		return 1
	else:
		return (n*(r-1))

for i in range(0,int(x)):
	ins = raw_input()
	ins = ins.split(" ")
	print("Case " + str(i+1) + ": " + str(better(int(ins[0]),int(ins[1]))))
