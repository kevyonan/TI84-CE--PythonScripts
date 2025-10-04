def simplify_rad(und_rt, root=2.0):
	und_rt = int(und_rt)
	if und_rt < 0:
		return None
	elif und_rt == 0 or und_rt == 1:
		return und_rt
	
	coef = 1
	
	# Check each factor from 2 up to sqrt(und_rt) to see if it can be taken out of the radical
	for i in range(2, int(und_rt ** (1/root)) + 1):
		pow_val = i ** root
		while und_rt % pow_val == 0:
			coef*=i
			und_rt//=pow_val
	
	return coef,und_rt

rv,rp=1.0,2.0
while rv>0.0:
	rp=float(input("enter root power: "))
	if rp<2.0:
		print("invalid power, retry")
		continue
	
	rv=float(input("enter root to simplify: "))
	if rv>0.0:
		coef,und=simplify_rad(rv, rp)
		print("solution is {coef} * root(^{rp}, {und})".format(coef=coef,rp=rp,und=und))