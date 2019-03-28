import math


def exp(x):
    return math.exp(x)

def func(x):
    
    mu = 1E-3
    cstar = 7.52E-7
    gamma = 4E-3
    C_0 = 1.05 * cstar

    xstar = 0.05

    C_1 = C_0 + mu * (xstar)**3

    Fn = mu * x*x*x + cstar * exp(gamma/x) - C_1

    dFn = 3 * mu * x*x - cstar * (gamma/(x*x)) * exp(gamma/x)
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

#maxIT = int(input("Max number of iterations? "))
#Tol = float(input("Tolerance for convergence? "))
#NumRoots = int(input("How many roots do you expect? "))

maxIT = 100
Tol = 1E-7
NumRoots = 2

for i in range(NumRoots):
    x0 = float(input("Initial guess for root number %d? " %(i+1)))
    rootfinder(x0, maxIT, Tol)









    
