from math import *

def simpsons(f, a, b):
	return ((b-a)/6.0) * (f(a) + (4*f((a+b) / 2.0)) + f(b))

def simpsons_iter(f, a, b, steps):
	h = (b - a) / steps;
	result = f(a) + f(b);
	
	for i in range(1, steps, 2):
		result += 4.0 * f(a + i * h)
	
	for i in range(1, steps-1, 2):
		result += 2.0 * f(a + i * h)
	
	return result * h / 3.0;

def run():
	cont = True
	while cont:
		b = float(input('enter "b" value: '))
		a = float(input('enter "a" value: '))
		c = 0
		reply = input('want steps? 1/0--: ')
		if len(reply) > 0 and reply[0]=='1':
			c += int(input('how many steps?: '))
		
		f = eval('lambda X: ' + input('write Python func: '))
		if c > 0:
			print(simpsons_iter(f, a, b, c))
		else:
			print(simpsons(f, a, b))
		
		reply = input('restart? (1-yes/0-no): ')
		cont = len(reply) > 0 and reply[0]=='1'

run()