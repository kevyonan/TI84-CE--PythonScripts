"""Copyright(2025) Kevin Yonan."""
#from math import *
from random import randint

def eval_csv(msg, as_tup=False):
	kb_str_input = input(msg)
	do_rand=0
	try:
		do_rand=int(kb_str_input)
	except(Exception):
		pass
	if do_rand>0:
		return list(randint(1, 100) for _ in range(do_rand))
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def get_mat():
	mat,prev=[],0
	while True:
		r=eval_csv("enter row, empty to stop: ")
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

def get_ijc(msg):
	a,b,c=0,0,0
	while True:
		entry=eval_csv("enter {}: ".format(msg), True)
		entry_len=len(entry)
		if entry_len<1:
			print("need at least one entry, try again")
			continue
		else:
			a=abs(entry[0])-1
			if entry_len>=2: b=entry[1]
			if entry_len>=3: c=entry[2]
			break
	return a,b,c

def deepcopy_mat(mat):
	copied_mat=[]
	for row in mat:
		copied_mat.append([i for i in row])
	return copied_mat

def fix_up_mat(m):
	widest=[]
	for col_idx in range(len(m[0])):
		width=0
		for row_idx in range(len(m)):
			m[row_idx][col_idx]=round(m[row_idx][col_idx],5)+0.0
			val_len=len(str(m[row_idx][col_idx]))
			if width<val_len: width=val_len
		widest.append(width)
	return widest

def mat_to_str(m):
	mat_str="\nCurr Matrix::\n"
	widest=fix_up_mat(m)
	for row_idx in range(len(m)):
		mat_str+="R{}|".format(row_idx+1)
		for col_idx in range(len(m[row_idx])):
			val=m[row_idx][col_idx]
			mat_str+="{b:>{a}}".format(a=widest[col_idx]+2,b=val)
		mat_str+="|\n"
	return mat_str

def run():
	cont=True
	msgs=("i & j","i, j, & c","i & c")
	while cont:
		M=get_mat()
		if len(M)<=0: continue
		undo_stk=[deepcopy_mat(M)]
		while True:
			print(mat_to_str(M))
			try:
				op=int(input("Row Ops::\n[1]Ri<=>Rj, [2]Ri+c*Rj, [3]Ri*c, [0]Undo Prev Op, [<0]Quit\nPick Op: "))
				if op==0:
					if len(undo_stk)>1:
						M=undo_stk.pop()
				elif op<=3 and op>=1:
					undo_stk.append(deepcopy_mat(M))
					i,j,c=get_ijc(msgs[abs(op-1)])
					if op<3:
						j=abs(j)-1
					if op==1:
						M[i],M[j]=M[j],M[i]
					else:
						for n in range(len(M[i])):
							if op==2:
								M[i][n]+=(c*M[j][n])+0.0
							else:
								M[i][n]*=j
				else:
					break
			except BaseException as err:
				print(err);continue
		cont=len(input("restart?: "))>0
run()


"""
Example:
-2,3,-1,1
1,0,1,0
-1,2,-2,0

Steps:
R2-R1,R3-R1,
R1<->R3,R3+R2,
R2-3*R1,R2*1/5,R3<->R2,
R2-R1,R1+R2,R1-R3,
R2-2R3


1st step: make leading 1 topmost [hint use Ri*c]
2nd step: use the leading 1 to add/subtract from other 
3rd step: make 2nd leading elem into 1 with Ri*c
4th step: repeat.

Start:
7 9 | 8
3 2 | 5

R1*(1/7):
1 9/7 | 8/7
3  2  |  5

R2 - 3R1:
1   9/7  |  8/7
0  -13/7 | 59/7

R2*(-7/13):
1   9/7 |   8/7
0    1  | -59/13

R2*(-7/13):
1   9/7 |   8/7
0    1  | -59/13

R1-(9/7)R2:
1   0 | 635/91
0   1 | -59/13
"""