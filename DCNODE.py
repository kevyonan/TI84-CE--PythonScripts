def eval_csv(msg):
	return eval('['+input(msg)+']')

def mat_idx(i,j,cols):
	return (i*cols)+j

def swap_rows(M, rows, cols, i, j):
	if i==j: return
	for k in range(cols): M[(i*cols)+k], M[(j*cols)+k] = M[(j*cols)+k], M[(i*cols)+k]

def scale_row(M, rows, cols, i, factor):
	for k in range(i*cols, (i*cols)+cols): M[k]*=factor

def add_mul_row(M, rows, cols, src, dst, factor):
	for k in range(cols): M[(dst*cols)+k]+=factor*M[(src*cols)+k]

def rref_aug(M, rows, cols):
	r=0
	for c in range(cols-1):
		pivot=-1
		max_abs=0.0
		for i in range(r, rows):
			if abs(M[i*cols+c]) > max_abs:
				max_abs=abs(M[i*cols+c])
				pivot=i
		if pivot==-1 or max_abs<1e-9: continue
		swap_rows(M, rows, cols, r, pivot)
		scale_row(M, rows, cols, r, 1.0/M[r*cols+c])
		for i in range(rows):
			if i!=r and abs(M[i*cols+c])>1e-9:
				add_mul_row(M, rows, cols, r, i, -M[i*cols+c])
		r+=1
		if r==rows: break

def stamp_resistors(M, N, cols):
	for _ in range(int(input("num Rs: "))):
		parts = eval_csv("R: N1 N2 Ohm: ")
		if len(parts)<3 or parts[2]==0: continue
		if parts[0] != 0: M[mat_idx(parts[0]-1, parts[0]-1, cols)] += 1.0/parts[2]
		if parts[1] != 0: M[mat_idx(parts[1]-1, parts[1]-1, cols)] += 1.0/parts[2]
		if parts[0] != 0 and parts[1] != 0:
			M[mat_idx(parts[0]-1, parts[1]-1, cols)] -= 1.0/parts[2]
			M[mat_idx(parts[1]-1, parts[0]-1, cols)] -= 1.0/parts[2]

def stamp_i_srcs(M, N, cols):
	for _ in range(int(input("num I srcs: "))):
		parts = eval_csv("I: N+ N- A: ")
		if len(parts)<3: continue
		if parts[0] != 0: M[mat_idx(parts[0]-1, cols-1, cols)] -= parts[2]
		if parts[1] != 0: M[mat_idx(parts[1]-1, cols-1, cols)] += parts[2]

def stamp_v_srcs(M, N, Nv, cols):
	if Nv==0: return
	print("put {} V srcs:".format(Nv))
	for k in range(Nv):
		parts = eval_csv("V{}: N+ N- V: ".format(k+1))
		if len(parts)<3: continue
		
		if parts[0] != 0: M[mat_idx(parts[0]-1, N+k, cols)] += 1.0
		if parts[1] != 0: M[mat_idx(parts[1]-1, N+k, cols)] -= 1.0
		
		if parts[0] != 0: M[mat_idx(N+k, parts[0]-1, cols)] += 1.0
		if parts[1] != 0: M[mat_idx(N+k, parts[1]-1, cols)] -= 1.0
		
		M[mat_idx(N+k, cols-1, cols)] += parts[2]


def run():
	print("DC Node-Voltage Solver\nBy Kevin Yonan")
	while True:
		N=int(input("num non-gnd nodes: "))
		Nv=int(input("num of voltage srcs: "))
		if N<=0: return
		cols=N+Nv+1
		try:
			M=[0.0]*((N+Nv)*cols)
			stamp_resistors(M, N, cols)
			stamp_i_srcs(M, N, cols)
			stamp_v_srcs(M, N, Nv, cols)
			rref_aug(M, N+Nv, cols)
			print("\nResults:")
			for i in range(N):
				print("V{} = {:g}\n".format(i+1,round(M[mat_idx(i, N+Nv, cols)],5)))
		except MemoryError:
			print("Mem Fail")
		if len(input("restart?: "))==0: break
run()