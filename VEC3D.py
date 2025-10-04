from math import *


unitv = ( (1,0,0), (0,1,0), (0,0,1) )


def mag(a):
	return sqrt(a[0]**2 + a[1]**2 + a[2]**2)

def dirangs(a, deg=0):
	length = mag(a)
	angles = acos(a[0]/length), acos(a[1]/length), acos(a[2]/length)
	if deg > 0:
		angles = (degrees(angles[0]), degrees(angles[1]), degrees(angles[2]))
	return angles

def norm(a):
	l = mag(a)
	return a[0]/l, a[1]/l, a[2]/l

def mul(a, scalar):
	return a[0]*scalar, a[1]*scalar, a[2]*scalar

## change vec's length while keeping direction.
def nlen(a, n):
	return mul(mul(a, n), 1/mag(a))


def add(a, b):
	return a[0]+b[0], a[1]+b[1], a[2]+b[2]

def sub(a, b):
	return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def dot(a, b):
	return (a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2])

def cross(a, b):
	return (a[1]*b[2] - a[2]*b[1]), (a[2]*b[0] - a[0]*b[2]), (a[0]*b[1] - a[1]*b[0])

def proj(a, b):
	return mul(b, dot(a,b) / (mag(b)**2))

# area of parallelogram
def parea(a, b):
	return mag(cross(a, b))

def ang(a, b, deg=0):
	ang = acos( dot(a, b) / (mag(a) * mag(b)) )
	if deg > 0:
		ang = degrees(ang)
	return ang

# equation of a line.
def line(a, m):
	pass

# equation of a plane.
def pln(a, N):
	pass

# distance btwn two point vecs.
def pdist(a, b):
	pass

# line distance
def ldist(a, pnt, m):
	pass
	
def pldist(a, pnt, m):
	pass

def boxvol(a, b, c):
	return dot(c, cross(a, b))


def get_vec_input(msg):
	while True:
		try:
			a = eval(input(msg + ": "))
			tuplen = len(a)
			if tuplen < 3:
				if tuplen==2:
					a = (a[0], a[1], 0.0)
				elif tuplen==1:
					a = (a[0], 0.0, 0.0)
			elif tuplen > 3:
				a = (a[0], a[1], a[2])
		except Exception as errA:
			print(errA, ":: try again")
		else:
			return a
	return None

def get_confirm_input(msg):
	while True:
		try:
			a = input(msg + ": ")[0]=='1'
		except Exception as err:
			print(err, ":: try again")
		else:
			return a
	return None

def get_input_vecs(inputs):
	a,b,c = None,None,None
	a = get_vec_input('enter "a" vec [write like "1,2,3"]:')
	if get_confirm_input('need a "b" vec? [1:Y|0:N]'):
		inputs[0] = True
		b = get_vec_input('enter "b" vec:')
		if get_confirm_input('need a "c" vec? [1:Y|0:N]'):
			inputs[1] = True
			c = get_vec_input('enter "c" vec:')
	
	return a,b,c

def run():
	cont = True
	while cont:
		inputs = [False, False]
		a, b, c = get_input_vecs(inputs)
		prompt = "enter Python code with a"
		if inputs[0]:
			if not inputs[1]:
				prompt += " and"
			prompt += " b"
			if inputs[1]:
				prompt += ", and c"
		print(prompt + ':')
		print("ops: norm(a), mag(a), dirangs(a, 1 for degrees), mul(a,scalar), nlen(a,scalar)")
		if inputs[0]:
			print("add(a,b), sub(a,b), dot(a,b), cross(a,b), proj(a,b), ang(a,b, 1 for degrees), parea(a,b)")
			if inputs[1]:
				print("boxvol(a,b,c)")
		
		do_math = True
		while do_math:
			lambda_str = "lambda a, b, c: "
			try:
				vec_f = eval(lambda_str + input())
				print(vec_f(a, b, c))
			except Exception as err:
				print(err, ":: try again")
			else:
				do_math = input("more math? (1-yes/0-no): ")[0]=='1'
		
		cont = input("continue? (1-yes/0-no): ")[0]=='1'
		do_math = True

run()