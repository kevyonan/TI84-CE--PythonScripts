import math

def get_opt_num(msg):
	return float(eval(input(msg)))

def get_opt_phz(msg):
	return complex(eval(input(msg)))

def get_phasor():
	if input("hit 1 to enter polar: ")=='1':
		return polar_to_rect(get_opt_num("enter ampl: "),get_opt_num("enter ph-ang: "))
	return get_opt_phz("enter rect phasor: ")

def eval_csv(msg):
	return eval('['+input(msg)+']')

def rnd(n, m=5):
	if isinstance(n,complex):
		return complex(rnd(n.real),rnd(n.imag))
	return round(n,m)

def rect_to_polar(j):
	if not isinstance(j,complex):
		return j,0.0
	return (j.real**2 + j.imag**2)**0.5, math.degrees(math.atan2(j.imag,j.real))

def polar_to_rect(ampl,ang):
	return complex(ampl*math.cos(math.radians(ang)),ampl*math.sin(math.radians(ang)))

def clamp_degs(d):
	return math.fmod(abs(d),360.0)

def run():
	cont=True
	while cont:
		opt=int(get_opt_num("Phasors:: 1-Impeds|2-Pwr|3-DY|4-PZ|5-VD|6-CD: "))
		if opt==1:
			subopt=int(get_opt_num("Impeds:: 1-L|2-C|3-R: "))
			v_max=get_opt_num("Enter Vmax [0 if none]: ")
			w=get_opt_num("Enter omega/w: ")
			if subopt==1:
				L=get_opt_num("Enter henries: ")
				print("Z_L = jwL = {}".format(rnd(w*L*1j)))
				if v_max != 0.0: print("0.5*Vmax^2/Z* = {}".format(rnd((0.5*(v_max**2))/(w*L*-1j))))
			elif subopt==2:
				C=get_opt_num("Enter farads: ")
				print("Z_C = 1/jwC = {}".format(rnd(1.0/(w*C*1j))))
				if v_max != 0.0: print("0.5*Vmax^2/Z* = {}".format(rnd((0.5*(v_max**2))/(1.0/(w*C*1j)))))
		elif opt==2:
			vals=eval_csv("Enter Vmax, Imax, V-theta, I-theta: ")
			a=(vals[0]*vals[1])/2.0
			vt_cos=clamp_degs(vals[2]) if input("v(t) has math.sin? [1-Y]: ")!='1' else clamp_degs(clamp_degs(vals[2])-90.0)
			it_cos=clamp_degs(vals[3]) if input("i(t) has math.sin? [1-Y]: ")!='1' else clamp_degs(clamp_degs(vals[3])-90.0)
			dtheta=math.radians(vt_cos-it_cos)
			print("a = [Vmax*Imax]/2 = {:g}".format(rnd(a)))
			print("pwr fctr = cos(dth) = {:g}".format(rnd(math.cos(dtheta))))
			print("react fctr = sin(dth) = {:g}".format(rnd(math.sin(dtheta))))
			print("avg power: a*pf = {:g}".format(rnd(a*math.cos(dtheta))))
			print("react pwr: a*rf = {:g}".format(rnd(a*math.sin(dtheta))))
			if dtheta<0.0: print("current leading")
			elif dtheta>0.0: print("current lagging")
		elif opt==3:
			# delta-to-Y/math.pi-to-T
			print("|---ZC---|\n|        |\nZB      ZA\n|        |\n|        |")
			zs=eval_csv("enter Zs in order ZA, ZB, ZC: ")
			if len(zs)<3:continue
			z_sum=zs[0]+zs[1]+zs[2]
			print("Z1 = {}\nZ2 = {}\nZ3 = {}".format(
				rnd((zs[1]*zs[2])/z_sum),
				rnd((zs[0]*zs[2])/z_sum),
				rnd((zs[0]*zs[1])/z_sum)
			))
			print("Z1--+--Z2\n    |    \n    |    \n    |    \n   Z3    ")
		elif opt==4:
			zs=eval_csv("enter parallel Zs: ")
			z_eq=0j
			if len(zs)==2: z_eq=(zs[0]*zs[1])/(zs[0]+zs[1])
			else:
				for z in zs:z_eq+=(1/z)
				z_eq=1/z_eq
			print("Z_eq of {} = {}".format(zs,rnd(z_eq)))
		elif opt==5:
			# voltage divider
			v=get_phasor()
			zs=eval_csv("enter Zs in series: ")
			z_eq=0j
			for z in zs:
				z_eq+=z
			for i in range(len(zs)):
				print("v{} = (Z_i/Z_eq)*V = {}".format(i+1,rnd((zs[i]/z_eq)*v)))
		elif opt==6:
			# current divider
			c=get_phasor()
			zs=eval_csv("enter Zs in parallel: ")
			z_eq=0j
			for z in zs:
				z_eq+=1/z
			z_eq=1/z_eq
			for i in range(len(zs)):
				print("i{} = (Z_eq/Z_i)*i = {}".format(i+1,rnd((z_eq/zs[i])*c)))
		cont=len(input("enter to exit: "))>0
run()