def squared_sum(vals, xbar):
	_sum = 0.0
	for val in vals:
		_sum += ((val - xbar)**2)
	return _sum

cont = True
while cont:
	N=eval(input("enter n: "))
	vals=[x for x in eval(input("enter values: "))]
	prec=int(input("num of decimal places?: "))
	x_bar=sum(vals)/N
	samp_var=squared_sum(vals, x_bar)/(N-1)
	print("x bar = {a:.{p}f}".format(p=prec, a=x_bar))
	print("S**2={a:.{p}f}, S={b:.{p}f}".format(p=prec, a=samp_var, b=samp_var**0.5))
	cont=len(input("continue?[any]: ")) > 0
