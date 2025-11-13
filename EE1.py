def get_opt_num(msg):
	opt=0.0
	try:opt+=float(input(msg))
	except:pass
	return opt

def eval_csv(msg):
	return eval('['+input(msg)+']')

def rnd(n, m=5):
	if isinstance(n,complex):
		return complex(rnd(n.real),rnd(n.imag))
	return round(n,m)

def run():
	cont=True
	while cont:
		opt=int(get_opt_num("Circuit Ops::1-VD|2-CD|3-DY|4-nRs: "))
		if opt==1:
			# voltage divider
			v=get_opt_num("enter volts: ")
			rs=eval_csv("enter Rs in series: ")
			r_eq=0
			for r in rs:
				r_eq+=r
			for i in range(len(rs)):
				print("v{} = (R_i/R_eq)*V = ({:g}/{:g})*{:g} = {:g}".format(i+1,rnd(rs[i]),rnd(r_eq),rnd(v),rnd((rs[i]/r_eq)*v)))
		elif opt==2:
			# current divider
			c=get_opt_num("enter current: ")
			rs=eval_csv("enter Rs in parallel: ")
			r_eq=0
			for r in rs:
				r_eq+=1/r
			r_eq=1/r_eq
			for i in range(len(rs)):
				print("i{} = (R_eq/R_i)*i = ({:g}/{:g})*{:g} = {:g}".format(i+1,rnd(rs[i]),rnd(r_eq),rnd(c),rnd((r_eq/rs[i])*c)))
		elif opt==3:
			# delta-to-Y/pi-to-T
			subopt = int(get_opt_num("Delta-To-Y::1-R|2-C|3-L: "))
			letter = 'R' if subopt==1 else 'L' if subopt==3 else 'C'
			print("|---{}C---|\n|        |\n{}B      {}A\n|        |\n|        |".format(letter,letter,letter))
			rs=eval_csv("enter vals in order {}A, {}B, {}C: ".format(letter,letter,letter))
			if len(rs)<3:continue
			if subopt != 2:
				r_sum=rs[0]+rs[1]+rs[2]
				print("{}1 = [{:g}*{:g}]/{:g} = {:g}\n{}2 = [{:g}*{:g}]/{:g} = {:g}\n{}3 = [{:g}*{:g}]/{:g} = {:g}".format(
					letter, rnd(rs[1]), rnd(rs[2]), rnd(r_sum), rnd((rs[1]*rs[2])/r_sum),
					letter, rnd(rs[0]), rnd(rs[2]), rnd(r_sum), rnd((rs[0]*rs[2])/r_sum),
					letter, rnd(rs[0]), rnd(rs[1]), rnd(r_sum), rnd((rs[0]*rs[1])/r_sum)
				))
			else:
				r_sum=(rs[0]*(rs[1]+rs[2]))+(rs[1]*rs[2])
				print("C1 = {:g}/{:g} = {:g}\nC2 = {:g}/{:g} = {:g}\nC3 = {:g}/{:g} = {:g}".format(
					rnd(r_sum), rnd(rs[0]), rnd(r_sum/rs[0]),
					rnd(r_sum), rnd(rs[1]), rnd(r_sum/rs[1]),
					rnd(r_sum), rnd(rs[2]), rnd(r_sum/rs[2])
				))
			print("{}1--+--{}2\n    |    \n    |    \n    |    \n   {}3    ".format(letter,letter,letter))
		elif opt==4:
			# parallel resistors.
			rs=eval_csv("enter parallel Rs: ")
			r_eq=0.0
			if len(rs)==2: r_eq=(rs[0]*rs[1])/(rs[0]+rs[1])
			else:
				for r in rs:r_eq+=1/r
				r_eq=1/r_eq
			print("R_eq of {} = {:g}".format(rs,rnd(r_eq)))
		cont=len(input("restart?: "))>0
run()