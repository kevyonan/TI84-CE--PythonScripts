from math import sqrt,exp,pi,degrees,atan,e

def get_opt_num(msg):
	opt=0.0
	try:opt+=float(input(msg))
	except:pass
	return opt

def eval_csv(msg, as_tup=False):
	kb_str_input=input(msg)
	do_rand=0
	try:do_rand=int(kb_str_input)
	except:pass
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def rnd(n, m=5):return round(n, m)

def run():
	cont=True
	while cont:
		opt=int(get_opt_num("Circuit Ops::1-LCWork|2-LCEq|3-Time: "))
		if opt==1:
			subopt=int(get_opt_num("WorkEq::0-GoBack|1-C|2-L: "))
			if subopt!=1 and subopt!=2:continue
			vals=eval_csv("enter {}: ".format("farads, volts" if subopt==1 else "henries, current"))
			if len(vals)<2:continue
			nrgy=0.5*vals[0]*vals[1]
			print("w = 0.5*{}^2 = {:g}".format("C*v" if subopt==1 else "L*i",nrgy))
		elif opt==2:
			subopt=int(get_opt_num("DiffEq::0-GoBack|1-RC|2-RL: "))
			if subopt!=1 and subopt!=2:continue
			vals=eval_csv("enter x0, xf: ")
			if len(vals)<2:continue
			tcs=eval_csv("enter ohms, {}: ".format("farads" if subopt==1 else "henries"))
			if len(tcs)<2:continue
			tc=tcs[0]*tcs[1] if subopt==1 else tcs[1]/tcs[0]
			eq=""
			if tc<1: eq="{:g} + {:g}*(e**-({:g}*t))".format(vals[1], vals[0]-vals[1], 1/tc)
			else:eq="{:g} + {:g}*(e**-(t / {:g}))".format(vals[1], vals[0]-vals[1], tc)
			print("X(t) =",eq)
			while int(get_opt_num("DiffEq::1-HasSeq?: "))==1:
				t1=get_opt_num("enter time: ")
				diff_eq=eval("lambda t:"+eq)
				x1o=diff_eq(t1)
				print("X({:g}) = {:g} = x1o".format(t1,x1o))
				x1f=get_opt_num("enter x1f: ")
				tcs=eval_csv("enter ohms, {}: ".format("farads" if subopt==1 else "henries"))
				if len(tcs)<2:continue
				tc=tcs[0]*tcs[1] if subopt==1 else tcs[1]/tcs[0]
				eq=""
				if tc<1: eq="{:g} + {:g}*e**-({:g}*t)".format(x1f, x1o-vals[1], 1/tc)
				else:eq="{:g} + {:g}*e**-(t / {:g})".format(x1f, x1o-x1f, tc)
				print("X(t) =",eq)
		elif opt==3:
			subopt=int(get_opt_num("Time::0-GoBack|1-FreqRC/RL|2-Vrms|3-X(T)|4-PhAng-dT|5-PhAngRC/RL: "))
			if subopt==1:
				tc=get_opt_num("enter time-const: ")
				print("freq = {:g}Hz".format( rnd(1/(10.58661*tc)) ))
			elif subopt==2:
				waveopt=int(get_opt_num("Waves::0-GoBack|1-Sq|2-Sin|3-Tri: "))
				v_max=get_opt_num("enter Vmax: ")
				rut=1
				if waveopt==2:rut+=1
				elif waveopt==3:rut+=2
				print("Vrms = {:g}".format(v_max/sqrt(rut)))
			elif subopt==3:
				vals=eval_csv("enter x0,xf: ")
				if len(vals)<2:continue
				diff=vals[0]-vals[1]
				print("X(Tau) = {:g} + {:g}*e^-1 = {:g}".format(vals[1],diff,vals[1]+(diff*exp(-1))))
			elif subopt==4:
				vals=eval_csv("enter freq, time-delay: ")
				if len(vals)<2:continue
				print("Ph-Angle = {:g} degs".format(vals[0]*vals[1]*360.0))
			elif subopt==5:
				circopt=int(get_opt_num("Time::0-GoBack|1-RC|2-RL: "))
				if circopt==0:continue
				vals=eval_csv("enter ohms, {}, freq: ".format("farads" if circopt==1 else "henries"))
				if len(vals)<3:continue
				x=-2.0*pi*vals[0]*vals[1]*vals[2] if circopt==1 else (2.0*pi*vals[1]*vals[2])/vals[0]
				print("Ph-Angle = {:g} degs".format(degrees(atan(x))))
			else:continue
		cont=len(input("restart?: "))>0
run()