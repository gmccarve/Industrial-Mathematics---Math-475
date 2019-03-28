import math
import numpy as np


def FCN(t, y1, y2):
    return y2, y1


"""t_0     = float(input("Initial time? "))
y_0     = float(input("Initial y-value? "))
t_end   = float(input("Final time? "))
N_steps = int(input("Number of steps? "))"""

t_0 = 0
y1_0 = 1
y2_0 = 0
t_end = 1
N_steps = 5000

ERRmax = 0.0

deltaT = (t_end - t_0) / (N_steps)


Y1_n = y1_0   #Initialize Y1_0 = y1_0
Y2_n = y2_0   #Initialize Y2_0 = y2_0

for n in range(0, N_steps + 1):
    
    t_n = t_0 + n * deltaT

    F1, F2 = FCN(t_n, Y1_n, Y2_n)
    
    Y1_nn = Y1_n + deltaT * F1
    Y2_nn = Y2_n + deltaT * F2
    
    Y1_n = Y1_nn
    Y2_n = Y2_nn

    Y1exact = np.cosh(t_n)
    Y2exact = np.sinh(t_n)

    #print (Y2_n, np.sinh(t_n))

    ERRn = abs(Y1exact - Y1_n)
    ERRmax = max(ERRn, ERRmax)

    #print (round(t_n,3), round(Y1_n,3), round(np.cosh(t_n),3), "%e" %ERRn)

print (Y1_n)
print ("%e" %ERRmax)
    
    

