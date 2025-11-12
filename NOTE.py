"""
Inductors & Capacitors:
V_L = L*di(t)/dt.
i_C = C*dV(t)/dt.

Energy Trapped:
w = 0.5*C*v^2 or 0.5*L*i^2.

Capacitor Voltage Divider:
V1,V2 = (Cn/Sum(Cs))*Vs -/+ Vo.
"""

"""
Op-Amps:
Assume In = Ip = 0.
Calc voltage at Vp.
Vp = Vn.
Use node-voltage method at Vn to calc voltage at Vo.
Check if Vo is in valid range.
Do one block at a time.

Inverting: Vo = -(Rf/Rs)Vs.
Summing: Vo = -Sum((Rf/Rn)Vn).
Non-Inverting: Vo = (1 + (Rf/Rn))Vx.
Difference: Vo = (1 + (Rf/Rs))Vb - (Rf/Rs)Va.

Differentiating: Vo = Rf*Ic
Ic = C*dV/Dt = C*d(0-Vs)/Dt = -C*dVs/Dt
Vo = -Rf*C*dVs/Dt.

Integrating:
Vo = Vn - Vc = -Vc
Ic = Vs/Rs
dVo/dt = -dVc/dt = -Vs/(Rs*C)
"""

"""
RL/RC Circuits:
time const = RC or L/R = T.
find xi & xf.
x(0-) = x(0+).
x(t) = xf + (xi - xf)*e^-( t-t0+ / T ).
"""

"""
RLC Circuits:
Parallel:
d^2*V(t)/dt^2 + 1/RC dV/dt + 1/LC V = 0.
C*dV(t)/dt + V/R + i_L(0+) = 0.
C*dV(t)/dt + V/R + i_L(0+) = i_s.
a = 1/2RC.

Series:
d^2*i(t)/dt^2 + R/L di/dt + 1/LC i = 0.
iR+L*di/dt + Vc = 0.
iR+L*di/dt + Vc = Vs.
a = R/2L.

w^2 = 1/LC.
b = a^2 - w^2.
s1,s2 = -a +/- sqrt(b).

if beta>0: overdamped, s1,s2 reals.
x(t) = xf + A1e^(s1*t) + A2e^(s2*t).
x(0+) = xf + A1 + A2.
dx(0+)/dt = s1*A1 + s2*A2.

if beta<0: underdamped, s1,s2 complex.
W = sqrt(|alpha^2 - w^2|).
x(t) = xf + A1*e^(-a*t)*cos(Wt) + A2*t*e^(-a*t)*sin(Wt).
x(0+) = xf + A1.
dx(0+)/dt = -a*A1 + W*A2.

if beta==0: crit damped, s1,s2 = -alpha.
x(t) = xf + A1*e^(-a*t) + A2*t*e^(-a*t).
x(0+) = xf + A1.
dx(0+)/dt = -a*A1 + A2.

di(0+)/dt = V(0+)/L.
dV(0+)/dt = i(0+)/C.
∂
"""

"""
f = 1/Period
w = 2*pi*f
V(t) = Vmax*cos(wt)
"""