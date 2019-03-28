

def func(x):
    return x*x-3, 2*x

def rootfinder(x0, maxIT, Tol):

    xn = float(x0)
    dx = 100
    print ("  n\txn\t\tFn")
    for n in range(1,maxIT):
        Fn, dFn = func(xn)
        print ("%3d\t%e\t%e" % (n,xn,Fn))
        if abs(dx) < Tol:
            if abs(Fn) < Tol:
                print ("\nDONE: root= %e, f= %e in %2d iterations" % (xn, Fn, n))
                return
            else:
                print ("STUCK: dx < Tol but residual = %16.14f > Tol" % (Fn))
                return
        dx = Fn/dFn
        xn = xn - dx

        
    return

x0 = float(input("Initial guess for the root? "))
maxIT = int(input("Max number of iterations? "))
Tol = float(input("Tolerance for convergence? "))

rootfinder(x0, maxIT, Tol)



