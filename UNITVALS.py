import math

def gcd(a, b):
	while b != 0:
		temp=a%b
		a=b
		b=temp
	return a

def gcf(a,b):
	return(a*b)//gcd(a,b)

def reduce_fract(_numer,_denom):
	return _numer//gcd(abs(_numer),_denom), _denom//gcd(abs(_numer),_denom)

def dec_to_fract(d,n=4):
	return int(round(d,n)*(10**n)),10**n

cont = True
while cont:
	numer,denom=0.0,180.0
	degree=float(input("enter degree: "))
	degree=math.fmod(degree,360.0)
	numer+=degree
	divisor=gcd(abs(numer),denom)
	numer,denom=reduce_fract(numer,denom)
	rad_str=""
	if numer!=1.0: rad_str+="{}*".format(numer)
	rad_str+="pi/{}".format(denom)
	print("{} in radians: {}".format(degree,rad_str))
	trig_funcs=(math.sin,math.cos,math.tan)
	trig_func_names=("sin","cos","tan")
	for i in range(len(trig_funcs)):
		trig_res=trig_funcs[i](math.radians(degree))
		print("{}({}): {:.5f}".format(trig_func_names[i],rad_str,trig_res))
	cont=len(input("restart? 1-Y: "))>0