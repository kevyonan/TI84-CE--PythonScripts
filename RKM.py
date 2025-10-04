def runge_kutta_4(f, t0, y0, t_end, h):
	t, y = t0, y0
	print('t0: ' + str(t) + '| y0: ' + str(y))
	i, eps = 1, 2.220446049250313e-16
	while t < t_end-eps:
		k1 = h * f(t, y)
		k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
		k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
		k4 = h * f(t + h, y + k3)
		
		y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
		t += h
		print('t' + str(i) + ': ' + str(t) + '| y' + str(i) + ': ' + str(y))
		input('press enter to continue: ')
		i += 1

def run():
	cont = True
	while cont:
		t0 = float(input('enter your "t" value: '))
		y0 = float(input('enter your "y" value: '))
		h = 0.2
		reply = input('want steps? 1/0: ')
		if len(reply) > 0 and reply[0]=='1':
			h = float(input('enter stepsize: '))
		
		t_end = int(input('enter end t: '))
		f = eval('lambda t, y: ' + input('write Python func dy/dt(t,y): '))
		
		runge_kutta_4(f, t0, y0, t_end, h)
		reply = input('restart? (1-yes/0-no): ')
		cont = len(reply) > 0 and reply[0]=='1'

run()