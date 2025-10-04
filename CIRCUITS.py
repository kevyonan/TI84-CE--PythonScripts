# for passive sign convention, think of mesh current equation with voltage source.
# if passive sign convention is negative, then flip power graph.

def get_opt_num(msg):
	opt=0.0
	try: opt+=float(input(msg))
	except Exception: pass
	return opt

def eval_csv(msg, as_tup=False):
	kb_str_input=input(msg)
	do_rand=0
	try: do_rand=int(kb_str_input)
	except Exception: pass
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def rnd(n, m=5): return round(n, m)

def run():
	cont=True
	while cont:
		opt=int(get_opt_num("Circuit Ops:: 1-VD|2-CD|3-DY|4-nRs: "))
		if opt==1:
			# voltage divider
			v=get_opt_num("enter voltage: ")
			rs=eval_csv("enter resistors in series: ")
			r_eq=0
			for r in rs:
				r_eq+=r
			for i in range(len(rs)):
				r_v=(rs[i]/r_eq)*v
				print("v{} = ({:g}/{:g})*{:g} = {:g}".format(i+1,rnd(rs[i]),rnd(r_eq),rnd(v),rnd(r_v)))
		elif opt==2:
			# current divider
			c=get_opt_num("enter current: ")
			rs=eval_csv("enter resistors in parallel: ")
			r_eq=0
			for r in rs:
				r_eq+=1/r
			r_eq=1/r_eq
			for i in range(len(rs)):
				r_c=(r_eq/rs[i])*c
				print("i{} = ({:g}/{:g})*{:g} = {:g}".format(i+1,rnd(rs[i]),rnd(r_eq),rnd(c),rnd(r_c)))
		elif opt==3:
			# delta-to-Y/pi-to-T
			print("|---RC---|\n|        |\nRB      RA\n|        |\n|        |")
			rs=eval_csv("enter resistors in order RA, RB, RC: ")
			if len(rs)!=3: continue
			r_sum=rs[0]+rs[1]+rs[2]
			print("R1 = [{:g}*{:g}]/{:g} = {:g}\nR2 = [{:g}*{:g}]/{:g} = {:g}\nR3 = [{:g}*{:g}]/{:g} = {:g}".format(rnd(rs[1]),rnd(rs[2]),rnd(r_sum),rnd((rs[1]*rs[2])/r_sum),rnd(rs[0]),rnd(rs[2]),rnd(r_sum),rnd((rs[0]*rs[2])/r_sum),rnd(rs[0]),rnd(rs[1]),rnd(r_sum),rnd((rs[0]*rs[1])/r_sum)))
			print("R1--+--R2\n    |    \n    |    \n    |    \n   R3    ")
		elif opt==4:
			# parallel resistors.
			rs=eval_csv("enter parallel resistors: ")
			r_eq=0.0
			is_same_nums=True
			for i in range(len(rs)):
				if rs[i] != rs[0]:
					is_same_nums=False
			if is_same_nums: r_eq=rs[0]/len(rs)
			elif len(rs)==2: r_eq=(rs[0]*rs[1])/(rs[0]+rs[1])
			else:
				for r in rs:
					r_eq+=1/r
				r_eq=1/r_eq
			print("R_eq of {} = {:g}".format(rs,rnd(r_eq)))
		cont=len(input("restart?: "))>0
run()