import math

def R(ampl,ang):
	return complex(ampl*math.cos(math.radians(ang)),ampl*math.sin(math.radians(ang)))

def polar(j):
	if not isinstance(j,complex):
		return j,0.0
	return (j.real**2+j.imag**2)**0.5, math.degrees(math.atan2(j.imag,j.real))

def eval_csv(msg):
	return eval('['+input(msg).replace(",j,",",1j,").replace(",j",",1j").replace("+j","+1j")+']')

def get_mat():
	mat,prev=[],0
	while True:
		r=eval_csv("enter row, empty to stop: ")
		if len(r)<=0: break
		elif prev>0 and prev!=len(r):
			print("row '{}' doesn't match prev row's len '{}'".format(prev,len(r)))
			continue
		prev=len(r)
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
	for c in range(len(A[i])): A[i][c]*=factor

def add_mul_row(A,src,dst,factor):
	for c in range(len(A[src])): A[dst][c]+=factor*A[src][c]

def rref_inplace(A, eps=1e-9):
	if len(A)==0: return 0
	r=0
	for c in range(len(A[0])):
		pivot=-1
		max_abs=0.0
		for i in range(r,len(A)):
			if abs(A[i][c])>max_abs:
				max_abs=abs(A[i][c])
				pivot=i
		if pivot==-1 or max_abs<eps: continue
		swap_rows(A,r,pivot)
		scale_row(A,r,1.0/A[r][c])
		for i in range(len(A)):
			if i!=r and abs(-A[i][c])>eps:
				add_mul_row(A,r,i,-A[i][c])
		r+=1
		if r==len(A): break


def fix_up_mat(m,p=False):
	widest=[]
	for col_idx in range(len(m[0])):
		width=0
		for row_idx in range(len(m)):
			m[row_idx][col_idx]=rnd(m[row_idx][col_idx])+0.0
			if p:
				ampl,ang=polar(m[row_idx][col_idx])
				val_len=len("{:g}<{:g}".format(rnd(ampl),rnd(ang)))
			else: val_len=len(str(m[row_idx][col_idx]))
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
		print(mat_to_str(mat,input("print polar? 1-Y: ")=="1"))
		cont=len(input("restart?: "))>0
run()

## 1,0,0,16-12j
## 0,0,1,-14-48j
## -5,3+1j,2,0