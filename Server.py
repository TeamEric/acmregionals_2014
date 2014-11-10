x = raw_input()
casen = 1
while x != 0:
	ans = 0
	x = x.split(" ")
	ins = raw_input()
	ins = ins.split(" ")
	s = 0
	while ans<int(x[0]) and  s<int(x[1]):
		s+=int(ins[ans])
		ans+=1
	if s>int(x[1]):
		ans-=1

	print("Case " + str(casen)+": " +str(ans))
	casen+=1
	x = 0
	try:
		x = raw_input()
		int(x.split(" ")[0])
	except:
		x = 0
		pass