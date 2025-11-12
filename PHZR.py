from math import pi,degrees,radians,sin,cos,atan2

def get_opt_num(msg):
	opt=0.0
	try:opt+=float(eval(input(msg)))
	except:pass
	return opt

def get_opt_phz(msg):
	opt=0j
	try:opt+=complex(eval(input(msg)))
	except:pass
	return opt

def get_phasor():
	b=0j
	if input("hit 1 to enter polar: ")=='1':
		ampl=get_opt_num("enter ampl: ")
		ang=get_opt_num("enter ph-ang: ")
		b+=polar_to_rect(ampl,ang)
	else:
		b+=get_opt_phz("enter rect phasor: ")
	return b

def eval_csv(msg, as_tup=False):
	kb_str_input=input(msg)
	do_rand=0
	try:do_rand=int(kb_str_input)
	except:pass
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')

def rnd(n, m=5):
	if isinstance(n,complex):
		return complex(rnd(n.real),rnd(n.imag))
	return round(n,m)

def rect_to_polar(j):
	return (j.real**2 + j.imag**2)**0.5, degrees(atan2(j.imag,j.real))

def polar_to_rect(ampl,ang):
	r=radians(ang)
	return complex(ampl*cos(r),ampl*sin(r))

def clamp_degs(d):
	while d>360.0: d-=360.0
	while d<0.0: d+=360.0
	return d

def run():
	cont=True
	while cont:
		opt=int(get_opt_num("Phasors:: 1-Impeds|2-Pwr|3-DY|4-PZ|5-VD|6-CD: "))
		if opt==1:
			subopt=int(get_opt_num("Impedance:: 1-L|2-C: "))
			w=get_opt_num("Enter omega/w: ")
			if subopt==1:
				L=get_opt_num("Enter henries: ")
				Z_L=w*L*1j
				print("Z_L = jwL = {}".format(rnd(Z_L)))
			elif subopt==2:
				C=get_opt_num("Enter farads: ")
				Z_c=1.0/(w*C*1j)
				print("Z_C = 1/jwC = {}".format(rnd(Z_c)))
		elif opt==2:
			vals=eval_csv("Enter Vmax, Imax, V-theta, I-theta: ")
			a=(vals[0]*vals[1])/2.0
			vt=clamp_degs(vals[2])
			it=clamp_degs(vals[3])
			v_sin=int(input("v(t) uses sin? [1-Y]: ")=='1')
			i_sin=int(input("i(t) uses sin? [1-Y]: ")=='1')
			
			vt_cos=vt if v_sin!=1 else clamp_degs(vt-90.0)
			it_cos=it if i_sin!=1 else clamp_degs(it-90.0)
			dtheta=radians(vt_cos-it_cos)
			pf,rf=cos(dtheta),sin(dtheta)
			print("a = [Vmax*Imax]/2 = {:g}".format(rnd(a)))
			print("pwr fctr = cos(θv-θi) = {:g}".format(rnd(pf)))
			print("react fctr = sin(θv-θi) = {:g}".format(rnd(rf)))
			print("avg power: a*pf = {:g}".format(rnd(a*pf)))
			print("react pwr: a*rf = {:g}".format(rnd(a*rf)))
			if dtheta<0.0:
				print("current leading")
			elif dtheta>0.0:
				print("current lagging")
		elif opt==3:
			# delta-to-Y/pi-to-T
			print("|---ZC---|\n|        |\nZB      ZA\n|        |\n|        |")
			zs=eval_csv("enter vals in order ZA, ZB, ZC: ")
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
			if len(zs)==2:z_eq=(zs[0]*zs[1])/(zs[0]+zs[1])
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
				z_v=(zs[i]/z_eq)*v
				print("v{} = (Z_i/Z_eq)*V = {}".format(i+1,rnd(z_v)))
		elif opt==6:
			# current divider
			c=get_phasor()
			zs=eval_csv("enter Zs in parallel: ")
			z_eq=0j
			for z in zs:
				z_eq+=1/z
			z_eq=1/z_eq
			for i in range(len(zs)):
				z_c=(z_eq/zs[i])*c
				print("i{} = (Z_eq/Z_i)*i = {}".format(i+1,rnd(z_c)))
		cont=len(input("enter to exit: "))>0
run()