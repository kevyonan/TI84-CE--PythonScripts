# P(A|B) = [P(B|A)*P(A)] / P(B)
# Total Prob Rule: P(A) = Σ(n)[ P(A|E_n)*P(E_n) ]
def total_prob_rule(givens, events):
	s = 0.0
	for i in range(len(givens)):
		s += givens[i] * events[i]
	return s

cont = True
while cont:
	given_probs = eval(input("Enter the probabilities for each P(A|E_n), comma sep: "))
	event_probs = eval(input("Enter the probabilities for each P(E_n), comma sep: "))
	if len(given_probs) != len(event_probs):
		print("number of probabilities do not match, try again.")
		continue
	prec=int(input("num of decimal places?: "))
	p_a = total_prob_rule(given_probs, event_probs)
	print("P(A)={a:.{p}f}".format(p=prec, a=p_a))
	
	for i in range(len(given_probs)):
		En_givenA = (given_probs[i] * event_probs[i]) / p_a
		print("P(E{d}|A)={a:.{p}f}".format(p=prec, a=En_givenA, d=i))
	
	reply = input("continue?[1]: ")
	cont = len(reply) > 0 and reply[0]=='1'