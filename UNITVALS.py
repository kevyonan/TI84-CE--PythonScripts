'''
how much memory is dedicated for the Python interpreter on the TI-Nspire CX II CAS vs TI-84 CE?
2MB of heap (vs ≈ 18KB on the CE)
And 202 stack/recursion levels (vs 28 on the CE)

32Kb RAM for CE
'''

from math import *

#eps = 2.220446049250313e-16

def gcd(a, b):
	while b != 0:
		temp = a % b
		a = b
		b = temp
	return a

def gcf(a,b):
	return (a*b) // gcd(a,b)

def reduce_fract(_numer, _denom):
	divisor = gcd(abs(_numer), _denom)
	_numer //= divisor
	_denom //= divisor
	return _numer, _denom

def dec_to_fract(d, n=4):
	tenth_pow = 10**n
	d = round(d, n) * tenth_pow
	return int(d), tenth_pow

cont = True
while cont:
	numer,denom = 0,180
	degree = float(input("enter desired degree to get unit values of: "))
	while degree > 360.0:
		degree -= 360.0
	
	numer = degree
	divisor = gcd(abs(numer), denom)
	numer, denom = reduce_fract(numer, denom)
	
	rad_str = "({n}*pi)/{d}".format(n=numer, d=denom)
	print("{deg} in radians is: {s}".format(deg=degree, s=rad_str))
	trig_funcs      = ( sin,   cos,   tan )
	trig_func_names = ('sin', 'cos', 'tan')
	for i in range(len(trig_funcs)):
		trig_res = trig_funcs[i](radians(degree))
		print("{name}({s}): {a:.5f}".format(name=trig_func_names[i], s=rad_str, a=trig_res))
	cont = input('restart? (1-yes/0-no): ')[0]=='1'
