from sympy import *
from sympy.vector import CoordSysCartesian
from math import e

N = CoordSysCartesian('N')
print(N.i)

class sigma(Function):
    @classmethod
    def eval(cls, w1, w2, x1, x2):
        return 1/(1+e**(-(w1*x1+w2*x2)))

print(sigma(1,1,1,1))
w1, w2, x1, x2 = symbols('w1 w2 x1 x2')
print(sigma.diff(w1))
