def rkm4(f,t0,y0,tf,h):
	t,y=t0,y0
	print("t0: {} | y0: {}".format(t,y))
	i,eps=1,2.220446049250313e-16
	half_h=0.5*h
	while t<(tf-eps):
		k1=h*f(t,y)
		k2=h*f(t+half_h,y+0.5*k1)
		k3=h*f(t+half_h,y+0.5*k2)
		k4=h*f(t+h,y+k3)
		
		y=y+(k1+2*k2+2*k3+k4)/6
		t+=h
		print("t{}: {} | y{}: {}".format(i,t,i,y))
		input("enter to continue: ")
		i+=1

def run():
	cont=True
	while cont:
		t0=float(input('enter "t0" value: '))
		y0=float(input('enter "y0" value: '))
		h=0.2
		stps=input("want steps? 1-Y: ")
		if len(stps)>0: h=float(input("enter stepsize: "))
		tf=int(input("enter end t: "))
		f=eval("lambda t, y: "+input("write Python func dy/dt(t,y): "))
		
		rkm4(f,t0,y0,tf,h)
		stps=input("restart? 1-Y: ")
		cont=len(stps)>0
run()