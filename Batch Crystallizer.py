##########   EULER #######
import math
import numpy as np

def exp(x):
    return math.exp(x)


def FCN(t, x_t):
        
    mu = 1E-5
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar
    K = 5.0E7
    
    xstar = 0.08

    C_1 = C_0 + mu * (xstar)**3

    Fn = K * (C_1 - mu*x_t**3 - cstar*exp(gamma/x_t))
    
    return Fn


"""def func(x_t):
    
    mu = 1E-5
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar
    K = 5.0E7
    
    xstar = 0.08

    C_1 = C_0 + mu * (xstar)**3

    Fn = K * (C_1 - mu*x_t**3 - cstar*exp(gamma/x_t))

    dFn = K * (-3*mu*x_t*x_t + cstar*(gamma/(x_t*x_t))*exp(gamma/x_t))
    
    return Fn, dFn"""

def Euler():
    
    t_n = np.dtype(np.int64)
    t_0 = 0.00
    y_0 = 0.05
    t_end = 0.1
    N_steps = 10000000

    ERRmax = 0.0

    deltaT = (t_end - t_0) / (N_steps)

    print (str(deltaT))

    Y_n = y_0   #Initialize Y_0 = y_0
    
    for n in range(0, N_steps + 1):
        t_n = np.float32(t_0 + n * deltaT)
        Y_nn = Y_n + deltaT * FCN(t_n, Y_n)
        Y_n = Y_nn

        if Y_n < 0:
            #print ("%.14f" %Y_n)
            print ("%.14f" %t_n)
            #print (t_n)
            return
        
        #print (round(t_n,6),  round(Y_n,7))

        file.write (str(round(t_n,14)) + '  ' +  str(round(Y_n,14)) + '\n')


np.set_printoptions(precision=15)

file = open("C:/Users/gavin/OneDrive/Math 475/Project 1/test.txt", "w")
Euler()
file.close()
    
    

####### NEWTON ########


"""def rootfinder(x0, maxIT, Tol):

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

#maxIT = int(input("Max number of iterations? "))
#Tol = float(input("Tolerance for convergence? "))
#NumRoots = int(input("How many roots do you expect? "))

maxIT = 1000
Tol = 1E-9
NumRoots = 2

for i in range(NumRoots):
    x0 = float(input("\nInitial guess for root number %d? " %(i+1)))
    rootfinder(x0, maxIT, Tol)"""









    
