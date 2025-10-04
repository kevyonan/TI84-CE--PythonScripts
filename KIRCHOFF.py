INVALID=0
VOLTAGE=1
CAPACITOR=2
RESISTOR=3
INDUCTOR=4
DEV_TYPE_NAMES=("INVALID","VOLTAGE","CAPACITOR","RESISTOR","INDUCTOR")

POL_POS=1
POL_NEG=-1

DEV_TYPE=0
DEV_VALUE=1
DEV_POL=2
DEV_LINKS=3
dev_data=[]


def get_str(msg,need_answer=True,invalids=[]):
	while need_answer:
		given=input(msg)
		if not (len(given)<=0 or given in invalids):
			break
	return given

def get_opt_num(msg):
	opt=0.0
	try:
		opt+=float(input(msg))
	except(Exception):
		pass
	return opt

def eval_csv(msg, as_tup=False):
	kb_str_input=input(msg)
	return eval('('+kb_str_input+')') if as_tup else eval('['+kb_str_input+']')


def add_dev(dev_type,dev_value,polarity):
	index=len(dev_data)
	dev_data.append((dev_type, dev_value, polarity, []))
	return index

def connect_devs(dev1_id,dev2_id):
	if max(dev1_id,dev2_id) >= len(dev_data):
		return False
	dev_data[dev1_id][DEV_LINKS].append(dev2_id)
	return True

def get_connected_devs(dev_id):
	return dev_data[dev_id][DEV_LINKS] if dev_id<len(dev_data) else []

# I = dQ/dt
def get_dev_equation(dev_id):
	dev_type=dev_data[dev_id][DEV_TYPE]
	# Resistor:  V = IR = [dQ/dt]*R | I = V/R
	# Capacitor: V = Q/C | I = C(dV/dt)
	# Inductor:  V = L(dI/dt) | I = (1/L)∫V(t)dt
	if dev_type>=VOLTAGE and dev_type<=INDUCTOR:
		return "{}".format(dev_data[dev_id][DEV_VALUE])
	return "0"

def pos_or_neg(dev_id):
	return " - " if dev_data[dev_id][DEV_POL]==POL_POS else " + "

# this is uses Johnson's DFS + Backtracking Algorithm.
# O([|V|+|E|][C+1])
def get_loops(dev_id):
	visited=[False]*len(dev_data)
	cycles,path=[],[]
	dfs(dev_id,dev_id,visited,cycles,path)
	return cycles

def dfs(dev_id,start_id,visited=None,cycles=[],path=[],f=None):
	visited[dev_id]=True
	path.append(dev_id)
	if f is not None:
		f(dev_id)
	for neighbor in get_connected_devs(dev_id):
		if not visited[neighbor] or neighbor not in path:
			dfs(neighbor,start_id,visited,cycles,path,f)
		else:
			cycle_start_index=path.index(neighbor)
			cycle=path[cycle_start_index:]
			cycles.append(cycle)
	path.pop()

def get_ids():
	got_ids=True
	while True:
		picked_from=eval_csv("IDs of dev [-1 to cancel]: ")
		for i in picked_from:
			if not isinstance(i, float|int):
				got_ids=False
		if got_ids!=False:
			print("invalid ID csv, try again.")
			continue
		return picked_from

initial_dev=None
cont = True
while cont:
	dev_type=int(get_str("dev type? [1:V,2:C,3:R,4:L]: "))
	if dev_type<VOLTAGE or dev_type>INDUCTOR:
		print("invalid dev type")
		continue
	elif initial_dev==None:
		initial_dev=dev_type
	
	dev_name,dev_pol=get_str("dev name: "),get_str("dev polarity? [-/+]: ")
	new_dev=add_dev(dev_type,dev_name,POL_POS if dev_pol=='+' else POL_NEG)
	print("\nLink dev from...")
	for i in range(len(dev_data)):
		print("id [{}]: {} | links: {}".format(i,dev_data[i][DEV_VALUE],get_connected_devs(i)))
	
	picked_from=get_ids()
	for i in picked_from:
		if connect_devs(i,new_dev):
			print("linked {} to {}".format(dev_data[i][DEV_VALUE],dev_data[new_dev][DEV_VALUE]))
	print("\nLink dev to...")
	for i in range(len(dev_data)):
		print("id [{}]: {} | links: {}".format(i,dev_data[i][DEV_VALUE],get_connected_devs(i)))
	
	picked_to=get_ids()
	for i in picked_from:
		if connect_devs(new_dev,i):
			print("linked {} to {}".format(dev_data[new_dev][DEV_VALUE],dev_data[i][DEV_VALUE]))
	
	cont=not(len(input("Stop adding components? [1-Y]: "))>0)

loops=get_loops(initial_dev)
print("Number of Loops in circuit :: {}".format(len(loops)))
for loop in loops:
	equation=""
	for dev in loop:
		equation+=pos_or_neg(dev)+get_dev_equation(dev)
	print(equation+" = 0")