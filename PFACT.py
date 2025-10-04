import math

'''
(x+a)^2 == (x+a)(x+a) == x^2+ax+ax+a^2 == x^2 + 2ax + a^2 => ax^2 + bx + c
a(x^2 + [b/a]x + [c/a])
a(x+m)(x+n)

m+n = [b/a]
(b/[2a] + C) + (b/[2a] - C) = [b/a]

m*n = [c/a]
(b/[2a] + C)(b/[2a] - C) = [c/a]
b/[2a]^2 - C^2 = [c/a]
C^2 = b/[2a]^2 - [c/a]
C = sqrt(b/[2a]^2 - [c/a])

m = b/[2a] + C
n = b/[2a] - C
---------------------------------------------------

(x+a)^3 == (x+a)(x+a)(x+a)
== (x+a)*(x^2+ax+ax+a^2) == x^3+a[x^2]+a[x^2]+a[x^2]+[a^2]x+[a^2]x+[a^2]x+a^3
== x^3 + 3*a(x^2) + 3*(a^2)x + a^3 => ax^3 + bx^2 + cx + d

a(x^3 + [b/a]x^2 + [c/a]x + [d/a])
a(x+m)(x+n)(x+o)
ex: (x+2)(x+3)(x+4) == x^3 + 9x^2 + 26x + 24

m+n+o = [b/a] | 2+3+4 == 9
B = b/[3a] | B = 9/[3a] = 3
(B+C) + (B-C) = [b/a] | 2+3+4 = 9

m*n + n*o + m*o = [c/a] | 2*3[6] + 3*4[12] + 2*4[8] = 26

m*n*o = [d/a] | 2*3*4 = 6*4 = 24
(B + C)(B - C) = [d/a]
(B - C)(B^2 + BC + C^2) = [d/a] | 3^3 - C^3 = 24
B^3 - C^3 = [d/a] | 27 - C^3 = 24, C = cbrt(3)

m = 2
n = 3
o = 4
---------------------------------------------------


(x+a)^4 == x^4 + 4a(x^3) + (6a^2)(x^2) + (4a^3)x + a^4 => ax^4 + bx^3 + cx^2 + dx + e
'''

def factor_quadratic(coeffs):
	half=0.5
	b_half=(coeffs[1]/coeffs[0])*half
	c_solve=coeffs[2]/coeffs[0]
	c_solution=((b_half**2)-c_solve)**half
	return b_half+c_solution, b_half-c_solution

eps = 2.220446049250313e-16
def run():
	cont=True
	while cont:
		coeffs=list(eval(input("enter your coefficient values: ")))
		if len(coeffs)>3:
			print("coeffs = {}".format(coeffs[:len(coeffs)-1]))
			m,n=factor_quadratic(coeffs)
			print("factor_quadratic({}) == m:{}, n:{}".format(coeffs,m,n))
		else:
			print(factor_quadratic(coeffs))
		reply = input("restart? (1-yes/0-no): ")
		cont = len(reply) > 0 and reply[0]=='1'

run()