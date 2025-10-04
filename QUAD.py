import math

'''
def combination(n, k):
	if k < 0 or k > n:
		return 0
	elif k==0 or k==n:
		return 1
	
	k = min(k, n - k)
	c = 1
	for i in range(k):
		c *= (n - i)
		c //= (i + 1)
	return c
'''

def factor_quadratic(coeffs):
	half=0.5
	b_half=(coeffs[1]/coeffs[0])*half
	c_solve=coeffs[2]/coeffs[0]
	c_solution=((b_half**2)-c_solve)**half
	return b_half+c_solution, b_half-c_solution

eps=2.220446049250313e-16
def run():
	cont=True
	while cont:
		coeffs=eval(input('enter your A, B, and C value: '))
		m,n=factor_quadratic(coeffs)
		if abs(coeffs[0]-1.0)<eps:
			print("(x + {})(x + {})".format(round(m,5),round(n,5)))
		else:
			print("{}(x + {})(x + {})".format(coeffs[0],round(m,5),round(n,5)))
		reply=input('restart? (1-yes/0-no): ')
		cont=len(reply)>0 and reply[0]=='1'

run()