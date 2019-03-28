import math


def FCN(t, y):
    return y
    #return 2*t


"""t_0     = float(input("Initial time? "))
y_0     = float(input("Initial y-value? "))
t_end   = float(input("Final time? "))
N_steps = int(input("Number of steps? "))"""

t_0 = 0
y_0 = 1
t_end = 1
N_steps = 1000

ERRmax = 0.0



deltaT = (t_end - t_0) / (N_steps)


Y_n = y_0   #Initialize Y_0 = y_0

for n in range(0, N_steps + 1):
    
    t_n = t_0 + n * deltaT
    Y_nn = Y_n + deltaT * FCN(t_n, Y_n)
    Y_n = Y_nn

    Yexact = math.exp(t_n)
    #Yexact = t_n*t_n + 1

    ERRn = abs(Yexact - Y_n)
    ERRmax = max(ERRn, ERRmax)

    #print (round(t_n,3), round(Y_n,3), round(math.exp(t_n),3))

print ("%e" %ERRmax)
    
    

