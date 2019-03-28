####    PDE SOLVER   #####

import os
import numpy as np
import math

def sqrt(x):
    return math.sqrt(x)
def erf(x):
    return math.erf(x)
def erfc(x):
    return math.erfc(x)

def INIT(a, b, D, M):

    U = np.zeros((M+2))

    return U

def PDE(F, dt, dx, U, time):

    U[0] = 1
    U[M+1] = erfc(0.5 * b / (sqrt(D * time)))

    for i in range(1,M+1):
        U[i] = U[i] + (dt/dx) * (F[i] - F[i+1])


    return U

def FLUX(dx, U, D):

    F[1]   = -D * (U[1]   - U[0]) / (dx / 2)
    F[M+1] = -D * (U[M+1] - U[M]) / (dx / 2)

    for i in range(2,M+1):

        F[i] = -D * (U[i] - U[i-1]) / dx
        
    return F

def OUTPUT(time, nsteps, M, ERR, x, U, uEXACT):

    print ("# Profile at time: %9.4f   nsteps = %6d" % (time, nsteps))
    print ("# Error up to this time: %15.6e" % (ERR))
        
    for i in range(0,M+2):
        print ("%12.4f %16.8g %16.8g" % (x[i], U[i], uEXACT[i]))
    print ("\n")
        
                                
    return

def MESH(a, b, M, dx):

    x = np.zeros((M+2))

    length = b - a

    x[0] = a
    x[M+1] = b

    for i in range(1, M+1):
        x[i] = dx * i - dx / 2.0

    return x

def COMPARE(x, U, D, M, time):

    ERR = 0
    M = int(M)

    uEXACT = np.zeros((M+2))

    for i in range(0,M+2):
        arg = 0.5 * x[i] / (sqrt(D*time))
        uEXACT[i] = erfc(arg)
        ERRi = abs( U[i] - uEXACT[i])
        ERR = max(ERRi, ERR)
    return uEXACT, ERR



dir_path = os.path.dirname(os.path.realpath(__file__))
data = open(str(dir_path) + "/Data.dat", "r")
lines_list = data.readlines()

MM, tend, dtout, t0 = lines_list[1].split()
factor, a, b, D = lines_list[3].split()
MM, tend, dtout, t0 = float(MM), float(tend), float(dtout), float(t0)
factor, a, b, D = float(factor), float(a), float(b), float(D)

dx = 1 / MM
M = int((b-a) * MM)

x = MESH(a, b, M, dx)

dtEXPL = (dx * dx) / (2 * D)
dt = factor * dtEXPL
dtout = max(dtout, dt)
tout = dtout

Nend = int(((tend - t0)/ dt) + 1)

U = INIT(a, b, D, M)
F = np.zeros((M+2))

time = t0

uEXACT, ERR = COMPARE(x, U, D, M, 0.00000001)

for nsteps in range(1,Nend+1):
    time  = nsteps * dt + t0

    F = FLUX(dx, U, D)

    U = PDE(F, dt, dx, U, time)   

    if time >= tend:
        OUTPUT(time, nsteps, M, ERR, x, U, uEXACT)
        print ("DONE, at time         = " + str(time))
        print ("      number of steps = " + str(nsteps))
        print ("      maximum error   = " + str(ERR))
        break

    elif time >= tout:
        uEXACT, ERR = COMPARE(x, U, D, M, time)
        OUTPUT(time, nsteps, M, ERR, x, U, uEXACT)
        tout += dtout




    


           
        







    
