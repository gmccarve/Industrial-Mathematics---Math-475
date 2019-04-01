import math
import numpy as np

def exp(x):
    return math.exp(x)


def FCN(t, x1_t, x2_t):
        
    mu = 1E-3
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar
    K = 5.0E7
    
    x1star = 0.05
    x2star = 0.09

    C_t = C_0 + mu * (x1star)**3 + mu * (x2star)**3 - mu * (x1_t)**3 - mu * (x2_t)**3

    Fn1 = K * (C_t - cstar*exp(gamma/x1_t))
    Fn2 = K * (C_t - cstar*exp(gamma/x2_t))

    
    return Fn1, Fn2

def FCN1(t, x_t):
        
    mu = 1E-3
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar
    K = 5.0E7
    
    xstar = 0.09

    C_1 = C_0 + mu * (xstar)**3 - mu * x_t**3

    Fn = K * (C_1 - cstar*exp(gamma/x_t))
    
    return Fn
    

def Euler():
    
    t_n = np.dtype(np.int64)
    t_0 = 0.00
    y1_0 = 0.05
    y2_0 = 0.09
    t_end = 0.1
    N_steps = 10000

    ERRmax = 0.0

    deltaT = (t_end - t_0) / (N_steps)

    print (str(deltaT))

    Y1_n = y1_0
    Y2_n = y2_0
    
    for n in range(0, N_steps + 1):
        
        if Y1_n > 0.0:
            t_n = np.float64(t_0 + n * deltaT)

            F1, F2 = FCN(t_n, Y1_n, Y2_n)
            
            Y1_nn = Y1_n + deltaT * F1
            Y2_nn = Y2_n + deltaT * F2
            
            Y1_n = Y1_nn
            Y2_n = Y2_nn
            
            if Y1_n > 0.0:
                file.write(str(t_n) + "  " + str(Y1_n) + "  " + str(Y2_n) + '\n')

            if Y1_n < 0.0:

                print ("%2.14f %2.14f" % (Y1_n, Y2_n))
                print ("%.14f" % t_n)
                Y_n = Y2_n
                Y1_n = 0.0

        elif Y1_n == 0.0:

            #file.write(str(t_n) + "  " + str(Y1_n) + "  " + str(Y2_n) + '\n')
            t_n = np.float64(t_0 + n * deltaT)
            Y_nn = Y_n + deltaT * FCN1(t_n, Y_n)
            Y_n = Y_nn


def func(x_t):
    
    mu = 1E-3
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar
    K = 5.0E7
    
    xstar = 0.095

    C_1 = C_0 + mu * (xstar)**3

    Fn = K * (C_1 - mu*x_t**3 - cstar*exp(gamma/x_t))

    dFn = K * (-3*mu*x_t*x_t + cstar*(gamma/(x_t*x_t))*exp(gamma/x_t))
    
    return Fn, dFn        

def rootfinder(x0, maxIT, Tol):

    xn = float(x0)
    dx = 100
    print ("  n\txn\t\tFn")
    for n in range(1,maxIT):
        Fn, dFn = func(xn)
        print ("%3d\t%16.14f\t%16.14f" % (n,xn,Fn))
        if abs(dx) < Tol:
            if abs(Fn) < Tol:
                print ("\nDONE: root= %16.14f, f= %16.14f in %2d iterations" % (xn, Fn, n))
                return
            else:
                print ("STUCK: dx < Tol but residual = %10.9f > Tol" % (Fn))
                return
        dx = Fn/dFn
        xn = xn - dx

        
    return


np.set_printoptions(precision=15)

file = open("C:/Users/gavin/OneDrive/Math 475/Project 2/Dis.txt", "w")
Euler()
#rootfinder(0.1, 10000, 1E-11)
file.close()
    








    
