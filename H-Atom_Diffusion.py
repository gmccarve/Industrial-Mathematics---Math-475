import math
import random
import numpy as np
import matplotlib.pyplot as plt

def sqrt(x):
    return math.sqrt(x)

def Distance(a,b):
    A = (a[0] - b[0])**2
    B = (a[1] - b[1])**2
    C = (a[2] - b[2])**2

    return sqrt(A + B + C)


def Diffusion():

    H2List = np.zeros((12,3))
    H_Atom = np.zeros((3))
    Dist = np.zeros((100))

    pHpH = 3.79

    COM  = np.zeros((3))

    R1 = 2E6
    R2 = 1.8E6

    Time = 0.0
    T_end = 0.001

    H2List[0]  = np.array((-pHpH,   0,               0))
    H2List[1]  = np.array((-pHpH/2, -sqrt(3)*pHpH/2, 0))
    H2List[2]  = np.array((pHpH/2,  -sqrt(3)*pHpH/2, 0))
    H2List[3]  = np.array((pHpH,    0,               0))
    H2List[4]  = np.array((pHpH/2,  sqrt(3)*pHpH/2,  0))
    H2List[5]  = np.array((-pHpH/2, sqrt(3)*pHpH/2,  0))
    H2List[6]  = np.array((0,       -(sqrt(pHpH**2 - (pHpH/2)**2) - sqrt(3)*pHpH/6),  sqrt(6)*pHpH/3))
    H2List[7]  = np.array((-pHpH/2, sqrt(3)*pHpH/6,  sqrt(6)*pHpH/3))
    H2List[8]  = np.array((pHpH/2,  sqrt(3)*pHpH/6,  sqrt(6)*pHpH/3))  
    H2List[9] = np.array((0,       -(sqrt(pHpH**2 - (pHpH/2)**2) - sqrt(3)*pHpH/6), -sqrt(6)*pHpH/3))
    H2List[10] = np.array((-pHpH/2, sqrt(3)*pHpH/6,  -sqrt(6)*pHpH/3))
    H2List[11] = np.array((pHpH/2,  sqrt(3)*pHpH/6,  -sqrt(6)*pHpH/3))

    
    file.write("14\n\nI  " + str(H_Atom[0]) + '  ' + str(H_Atom[1]) + '  ' + str(H_Atom[2]) + '\n')
    file.write("U 0 0 0 \n")
    for i in range(0,12):
        file.write("He   " + str(H2List[i][0]) + '  ' + str(H2List[i][1]) + '  ' + str(H2List[i][2]) + '\n')


    while Time < T_end:
        
        T1 = -math.log(random.uniform(0,1)) / R1
        T2 = -math.log(random.uniform(0,1)) / R2

        if T1 < T2:
           Pos = random.randint(0,5)
           H_Atom = H_Atom + H2List[Pos]
           Time = Time + T1

        else:
            Pos = random.randint(6,11)
            H_Atom = H_Atom + H2List[Pos]
            Time = Time + T2

        file.write("14\n\nI  " + str(H_Atom[0]) + '  ' + str(H_Atom[1]) + '  ' + str(H_Atom[2]) + '\n')
        file.write("U 0 0 0 \n")
        for i in range(0,12):
            file.write("He   " + str(H2List[i][0] + H_Atom[0]) + '  ' + str(H2List[i][1] + H_Atom[1]) + '  ' + str(H2List[i][2] + H_Atom[2]) + '\n')
 

    return Distance(COM,H_Atom)


file = open("C:/Users/gavin/OneDrive/Math 475/Group Project/Dist.xyz", "w")
file1 = open("C:/Users/gavin/OneDrive/Math 475/Group Project/Dist.txt", "w")

Dist = np.zeros((1))

for i in range(10):
    print (i)
    Dis = Diffusion()
    file1.write(str(Dis) + '\n')
    Dist[i] = Dis

file.close()
file1.close()

plt.hist(Dist, 50)
plt.show()





   


        


