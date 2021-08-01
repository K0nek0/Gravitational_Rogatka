import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# t = np.arange(0, 100, 1)
# def bio(N, t):
#     dNdt = k*N
#     return dNdt

# N_0 = 1
# k = 0.05
# solve = odeint(bio, N_0, t)

# plt.plot(t, solve[:,0], color='green')


# def euler_1(n=100, h=1, t=0, N=1, k=.05):
#     N_ar = []
#     t_ar = []
#     N_ar.append(N)
#     t_ar.append(t)

#     for i in range(n):
#         N += h * k*N
#         t += h
#         N_ar.append(N)
#         t_ar.append(t)
#     return N_ar, t_ar

# plt.plot(euler_1()[1], euler_1()[0], color='blue')
# plt.show()



# t = np.arange(0 , 15, 0.001)
# def investicii(N, t):
#     dNdt = -k*N*t
#     return dNdt

# N_0 = 1000
# k = 0.08
# solve = odeint(investicii, N_0, t)

# plt.plot(t, solve[:,0], color='green')


# def euler_2(n=15, h=1, t=0, N=1000, k=.08):
#     N_ar = []
#     t_ar = []
#     N_ar.append(N)
#     t_ar.append(t)

#     for i in range(n):
#         N += h * -k*N*t
#         t += h
#         N_ar.append(N)
#         t_ar.append(t)
#     return N_ar, t_ar
    
# plt.plot(euler_2()[1], euler_2()[0], color='blue')
# plt.show()



# t = np.arange(0 , 100, 0.1)
# def shtuka(v, t):
#     dvdt = (F - y*v**2)/m
#     return dvdt

# F = 100
# y = 0.05
# v_0 = 0
# m = 100
# solve = odeint(shtuka, v_0, t)

# plt.plot(t, solve[0:,0])


# def euler_3(n=100, h=1, t=0, v=0, F=100, y=.05, m=100):
#     v_ar = []
#     t_ar = []
#     v_ar.append(v)
#     t_ar.append(t)

#     for i in range(n):
#         v += h * (F - y*v**2)/m
#         t += h
#         v_ar.append(v)
#         t_ar.append(t)
#     return v_ar, t_ar

# plt.plot(euler_3()[1], euler_3()[0], color='green')
# plt.show()



t = np.arange(0, 20, 0.01)
def dif(z,t):
    y, omega = z
    dy_dt = omega
    domega_dt = np.sin(-y)*omega-3*y*t-5
    return dy_dt, domega_dt

y0 = 0.01
omega0 = 0.05
z0 = y0, omega0
sol = odeint(dif, z0, t)
print(sol[:,1])
# plt.plot(t, sol[:,0])
# plt.plot(t, sol[:,1])
# plt.plot(sol[:,1], sol[:,0])


def euler_4(n=20, h=.01, t=0, y=.01, omega=.05):
    y_ar=[]
    omega_ar=[]
    t_ar=[]
    y_ar.append(y)
    omega_ar.append(omega)
    t_ar.append(t)

    for i in range(n):
        y += h * omega
        omega += h * (np.sin(-y)*omega-3*y*t-5)
        t += h
        y_ar.append(y)
        omega_ar.append(omega)
        t_ar.append(t)
    return y_ar, omega_ar, t_ar
print(euler_4()[1])
plt.plot(euler_4()[1], euler_4()[0], color='blue')
plt.show()
