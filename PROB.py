cont = True
while cont:
	AandB,total,Atot,Btot=eval(input("enter AnB, total, A total, and B total: "))
	prec=int(input("num of decimal places?: "))
	A,B= Atot-AandB, Btot-AandB
	U=total-(A+B+AandB)
	Acirc,Bcirc= A+AandB, B+AandB
	_a, _b, _aANDb= Acirc/total, Bcirc/total, AandB/total
	print("P(A)={a:.{p}f}, P(A')={b:.{p}f}".format(p=prec, a=_a, b=1-_a))
	print("P(B)={a:.{p}f}, P(B')={b:.{p}f}".format(p=prec, a=_b, b=1-_b))
	
	print("P(AnB)={a:.{p}f}, P(A'uB'=(AnB)')={b:.{p}f}".format(p=prec, a=_aANDb, b=1-(_aANDb)))
	print("P(AuB)={a:.{p}f}, P(A'nB'=(AuB)')={b:.{p}f}".format(p=prec, a=((_a)+(_b)-(_aANDb)), b=1-((_a)+(_b)-(_aANDb))))
	
	input("press enter for more:")
	print("P(A'uB)={a:.{p}f}, P(AuB')={b:.{p}f}".format(p=prec, a=(Bcirc+U)/total, b=(Acirc+U)/total))
	print("P(A'nB)={a:.{p}f}, P(AnB')={b:.{p}f}".format(p=prec, a=B/total, b=A/total))
	
	print("P(A|B)={a:.{p}f}, P(A'|B)={b:.{p}f}".format(p=prec, a=(_aANDb)/(_b), b=1-((_aANDb)/(_b))))
	print("P(A|B')={a:.{p}f}, P(A'|B')={b:.{p}f}".format(p=prec, a=(A/total)/(1-(_b)), b=(1-((_a)+(_b)-(_aANDb)))/(1-(_b))))
	
	input("press enter for more:")
	print("P(B|A)={a:.{p}f}, P(B'|A)={b:.{p}f}".format(p=prec, a=(_aANDb)/(_a), b=1-((_aANDb)/(_a))))
	print("P(B|A')={a:.{p}f}, P(B'|A')={b:.{p}f}".format(p=prec, a=(B/total)/(1-_a), b=(1-((_a)+(_b)-(_aANDb)))/(1-(_a))))
	
	reply=input("continue?[1]: ")
	cont=len(reply)>0 and reply[0]=='1'