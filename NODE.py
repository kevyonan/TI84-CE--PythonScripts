def get_opt_num(msg):
	opt = 0.0
	try:
		opt += float(input(msg))
	except Exception:
		pass
	return opt

def eval_csv(msg, as_tup=False):
	kb_str_input = input(msg)
	do_rand = 0
	try:
		do_rand = int(kb_str_input)
	except Exception:
		pass
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def rnd(n, m=5): return round(n, m)
def IJ(i, j, size): return (i * size) + j
def zfill(m): return [0.0]*m

def mat_rref(A, b, n):
	for col in range(n):
		piv = col
		piv_val = A[IJ(piv, col, n)]
		for r in range(col + 1, n):
			v = A[IJ(r, col, n)]
			if abs(v) > abs(piv_val):
				piv = r
				piv_val = v
		
		if abs(piv_val) < 1e-15:
			raise ValueError("single mat")
		
		if piv != col:
			base_c = col * n
			base_p = piv * n
			for j in range(n):
				A[base_c + j], A[base_p + j] = A[base_p + j], A[base_c + j]
			b[col], b[piv] = b[piv], b[col]
		
		pv = A[IJ(col, col, n)]
		inv_pv = 1.0 / pv
		base = col * n
		for j in range(col, n):
			A[base + j] *= inv_pv
		
		b[col] *= inv_pv
		for r in range(col + 1, n):
			f = A[IJ(r, col, n)]
			if f == 0.0:
				continue
			base_r = r * n
			for j in range(col, n):
				A[base_r + j] -= f * A[base + j]
			b[r] -= f * b[col]
			A[IJ(r, col, n)] = 0.0
	
	for i in range(n-1, -1, -1):
		acc = b[i]
		rowi = i * n
		for j in range(i + 1, n):
			acc -= A[rowi + j] * b[j]
		b[i] = acc

def node_voltage_mode():
	print("\nNode-Voltage DC Solver")
	N = 0
	while N <= 0 or N > 5:
		N = int(get_opt_num("num of non-gnd nodes (1..5): "))
	
	G = zfill(N*N)
	Ivec = zfill(N)
	mR = int(get_opt_num("num resistors: "))
	for k in range(mR):
		n1, n2, r = eval_csv("R"+str(k+1)+" (n1,n2,Ohms): ", as_tup=True)
		if r==0.0:
			print("R=0 ignored")
			continue
		g = 1.0 / r
		if n1 != 0:
			i = n1 - 1
			G[IJ(i, i, N)] += g
		if n2 != 0:
			j = n2 - 1
			G[IJ(j, j, N)] += g
		if n1 != 0 and n2 != 0:
			i = n1 - 1; j = n2 - 1
			G[IJ(i, j, N)] -= g
			G[IJ(j, i, N)] -= g
	
	mI = int(get_opt_num("num current srcs: "))
	for k in range(mI):
		np_, nm_, amp = eval_csv("I"+str(k+1)+" (n+,n-,Amps): ", as_tup=True)
		if np_ != 0:
			Ivec[np_-1] -= amp
		if nm_ != 0:
			Ivec[nm_-1] += amp
	
	mV = int(get_opt_num("num of voltage srcs: "))
	vs_np,vs_nm,vs_val = zfill(mV),zfill(mV),zfill(mV)
	for k in range(mV):
		a, b_, v = eval_csv("V"+str(k+1)+" (n+,n-,Volts): ", as_tup=True)
		vs_np[k] = int(a)
		vs_nm[k] = int(b_)
		vs_val[k] = v
	
	dim = N + mV
	M = zfill(dim*dim)
	b = zfill(dim)
	
	for r in range(N):
		rowr = r * dim
		gr = r * N
		for c in range(N):
			M[rowr + c] = G[gr + c]
	
	for k in range(mV):
		n_plus = vs_np[k]
		n_minus = vs_nm[k]
		if n_plus != 0:
			M[IJ(n_plus-1, N + k, dim)] += 1.0
		if n_minus != 0:
			M[IJ(n_minus-1, N + k, dim)] -= 1.0
	
	for k in range(mV):
		n_plus = vs_np[k]
		n_minus = vs_nm[k]
		row = N + k
		if n_plus != 0:
			M[IJ(row, n_plus-1, dim)] += 1.0
		if n_minus != 0:
			M[IJ(row, n_minus-1, dim)] -= 1.0
	
	for i in range(N):
		b[i] = Ivec[i]
	for k in range(mV):
		b[N + k] = vs_val[k]
	
	try:
		mat_rref(M, b, dim)
	except Exception as e:
		print("solve failed:", e)
		return
	
	print("\nResults:")
	for i in range(N):
		print("V"+str(i+1)+" =", rnd(b[i], 6), "V")
	if mV > 0:
		print("(currents thru voltage srcs, flows from n+ => n-)")
		for k in range(mV):
			print("I(V"+str(k+1)+") =", rnd(b[N+k], 5), "A")

def run():
	cont=True
	while cont:
		node_voltage_mode()
		cont=len(input("restart?: "))>0
run()