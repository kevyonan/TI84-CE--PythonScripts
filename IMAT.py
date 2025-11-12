from math import radians,degrees,atan2,cos,sin

def get_opt_num(msg):
	opt=0.0
	try:opt+=float(input(msg))
	except Exception:pass
	return opt

def R(ampl,ang):
	r=radians(ang)
	return complex(ampl*cos(r),ampl*sin(r))

def polar(j):
	if not isinstance(j,complex):
		return j,0.0
	return (j.real**2 + j.imag**2)**0.5, degrees(atan2(j.imag,j.real))

def eval_csv(msg,as_tup=False):
	kb_str_input=input(msg)
	kb_str_input=kb_str_input.replace(",j,",",1j,")
	kb_str_input=kb_str_input.replace(",j",",1j")
	kb_str_input=kb_str_input.replace("+j","+1j")
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def get_mat():
	mat,prev=[],0
	while True:
		r=eval_csv("enter row,empty to stop: ")
		curr=len(r)
		if curr<=0:
			break
		elif prev>0 and prev!=curr:
			print("given row '{}' doesn't match prev row's size '{}'".format(prev,curr))
			continue
		prev=curr
		mat.append(r)
		print("you gave: {} | curr mat size: {}".format(r,len(mat)))
	return mat

def rnd(n,m=5):
	if isinstance(n,complex):
		return complex(rnd(n.real),rnd(n.imag))
	return round(n,m)


def swap_rows(A,i,j):
	if i!=j: A[i],A[j]=A[j],A[i]

def scale_row(A,i,factor):
	row=A[i]
	for c in range(len(row)): row[c]*=factor

def add_row_multiple(A,src,dst,factor):
	src_row,dst_row=A[src],A[dst]
	for c in range(len(src_row)): dst_row[c]+=factor*src_row[c]

def rref_inplace(A,eps=1e-9):
	rows=len(A)
	if rows==0: return 0
	cols=len(A[0])
	r=0
	for c in range(cols):
		pivot=-1
		max_abs=0.0
		for i in range(r,rows):
			v=A[i][c]
			av=abs(v)
			if av>max_abs:
				max_abs=av
				pivot=i
		if pivot==-1 or max_abs<eps: continue
		swap_rows(A,r,pivot)
		pv=A[r][c]
		inv=1.0/pv
		scale_row(A,r,inv)
		for i in range(rows):
			if i!=r:
				factor=-A[i][c]
				if abs(factor)>eps: add_row_multiple(A,r,i,factor)
		r+=1
		if r==rows: break


def fix_up_mat(m,p=False):
	widest=[]
	for col_idx in range(len(m[0])):
		width=0
		for row_idx in range(len(m)):
			m[row_idx][col_idx]=rnd(m[row_idx][col_idx])+0.0
			if p:
				ampl,ang=polar(m[row_idx][col_idx])
				val_len=len("{:g}<{:g}".format(rnd(ampl),rnd(ang)))
			else:val_len=len(str(m[row_idx][col_idx]))
			if width<val_len: width=val_len
		widest.append(width)
	return widest

def mat_to_str(m,p=False):
	mat_str="\nCurr Matrix::\n"
	widest=fix_up_mat(m,p)
	for row_idx in range(len(m)):
		mat_str+="R{}|".format(row_idx+1)
		for col_idx in range(len(m[row_idx])):
			val=""
			if p:
				ampl,ang=polar(m[row_idx][col_idx])
				val="{:g}<{:g}".format(rnd(ampl),rnd(ang))
			else:
				val=str(m[row_idx][col_idx])
			mat_str+="{b:>{a}}".format(a=widest[col_idx]+2,b=str(val))
		mat_str+="|\n"
	return mat_str

def run():
	cont=True
	while cont:
		mat=get_mat()
		rref_inplace(mat)
		p=input("print polar? 1-Y: ")=="1"
		print(mat_to_str(mat,p))
		cont=len(input("restart?: "))>0
run()

"""
1,0,0,16-12j
0,0,1,-14-48j
-5,3+1j,2,0
"""