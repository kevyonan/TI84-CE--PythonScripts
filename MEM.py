## Mem Optimization Advice for TI84 CE Plus
## * Use as little temporaries as possible.
## * Only import library name, not its items.
## * Do not use doc-strings as comments.
## * Use flat lists.
## * 
## * 
## * 
## * 
## * 
## * 

def probe_mem(max_len):
	size=0
	block=None
	try:
		while size<=max_len:
			size+=1
			block=[0j]*size
		return size
	except MemoryError:
		return size-1

print("Approx max list length:", probe_mem(2000))