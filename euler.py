import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0, 100, 1)

def bio(N, t):
    dNdt = k*N
    return dNdt

N_0 = 1
k = 0.05

solve = odeint(bio, N_0, t)

plt.plot(t, solve[:,0], color='green')


def euler_1(n=100, h=1, t=0, N=1, k=.05):
    N_ar = []
    t_ar = []
    N_ar.append(N)
    t_ar.append(t)

    for i in range(n):
        N += h * k*N
        t += h
        N_ar.append(N)
        t_ar.append(t)
    return N_ar, t_ar
    
plt.plot(euler_1[1], euler_1[0], color='blue')
plt.show()