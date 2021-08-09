import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

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



# t = np.arange(0, 20, 0.01)
# def dif(z,t):
#     y, omega = z
#     dy_dt = omega
#     domega_dt = np.sin(-y)*omega-3*y*t-5
#     return dy_dt, domega_dt

# y0 = 0.01
# omega0 = 0.05
# z0 = y0, omega0
# sol = odeint(dif, z0, t)

# plt.plot(t, sol[:,0])
# plt.plot(t, sol[:,1])
# plt.plot(sol[:,1], sol[:,0], color='red')


# def euler_4(n=1500, h=.01, t=0, y=.01, omega=.05):
#     y_ar=[]
#     omega_ar=[]
#     t_ar=[]
#     y_ar.append(y)
#     omega_ar.append(omega)
#     t_ar.append(t)

#     for i in range(n):
#         y += h * omega
#         omega += h * (np.sin(-y)*omega-3*y*t-5)
#         t += h
#         y_ar.append(y)
#         omega_ar.append(omega)
#         t_ar.append(t)
#     return y_ar, omega_ar, t_ar

# plt.plot(euler_4()[1], euler_4()[0], color='blue')



# t=np.arange(0,100,0.1)
# def strong(z,t):
#     x,v_x,y,v_y = z
#     dxdt = v_x
#     dv_xdt = (F1 + F2*np.cos(A) + F3*np.cos(2*A) + F4*np.cos(3*A))/m
#     dydt = v_y
#     dv_ydt = (F4 + F3*np.sin(A) + F2*np.sin(2*A) + F1*np.sin(3*A))/m
#     return dxdt, dv_xdt, dydt, dv_ydt

# x0 = 0
# v_x0 = 10
# y0 = 0
# v_y0 = -30
# z0 = x0, v_x0, y0, v_y0
# F1 = 10
# F2 = 10
# F3 = 10
# F4 = 10
# m = 50
# A = 0.5235987756

# def solve_func(i, key):
#     sol = odeint(strong, z0, t)
#     if key == 'point':
#         x = sol[i, 0]
#         y = sol[i, 2]
#     else:
#         x = sol[:i, 0]
#         y = sol[:i, 2]
#     return x, y

# fig, ax = plt.subplots()
# ball, = plt.plot([], [], 'o', color='b')
# ball_line, = plt.plot([], [], '-', color='b')

# def animate(i):
#     ball.set_data(solve_func(i, 'point'))
#     ball_line.set_data(solve_func(i, 'line'))

# ani=FuncAnimation(fig, animate, 500, interval=30)
# plt.axis('equal')
# edge = 2000
# ax.set_xlim(-edge, edge)
# ax.set_ylim(-edge, edge)


def euler_5(n=1000, h=.1, t=0, x=0, vx=10, y=0, vy=-30,
            F1=10, F2=10, F3=10, F4=10, m=50, A = 0.5235987756):
    x_ar=[]
    vx_ar=[]
    y_ar=[]
    vy_ar=[]
    t_ar=[]
    x_ar.append(x)
    vx_ar.append(vx)
    y_ar.append(y)
    vy_ar.append(vy)
    t_ar.append(t)

    for i in range(n):
        x += h * vx
        vx += h * ((F1 + F2*np.cos(A) + F3*np.cos(2*A) + F4*np.cos(3*A))/m)
        y += h * vy
        vy += h * ((F4 + F3*np.sin(A) + F2*np.sin(2*A) + F1*np.sin(3*A))/m)
        t += h
        x_ar.append(x)
        vx_ar.append(vx)
        y_ar.append(y)
        vy_ar.append(vy)
        t_ar.append(t)
    return x_ar, vx_ar, y_ar, vy_ar, t_ar

def solve_func(i, key):
    if key == 'point':
        x = euler_5()[0][i]
        y = euler_5()[2][i]
    else:
        x = euler_5()[0][:i]
        y = euler_5()[2][:i]
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='b')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani=FuncAnimation(fig, animate, 500, interval=30)
plt.axis('equal')
edge = 2000
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
plt.show()