def nmethod(f, df, x0, tol=1e-6, max_iter=100):
	x = x0
	num_iter = 1
	print('x0: ' + str(x))
	while abs(f(x)) > tol and num_iter < max_iter:
		x = x - f(x) / df(x)
		print('x' + str(num_iter) + ': ' + str(x))
		num_iter += 1
		input('press enter to continue: ')

def run():
	cont = True
	print('Newton-Raphson Method: starting at x = 1')
	while cont:
		f = eval('lambda X: ' + input('write in Python your f(X): '))
		df = eval('lambda X: ' + input('write in Python your df(X): '))
		nmethod(f, df, 1)
		cont = input('restart? (1-yes/0-no): ')[0]=='1'

run()