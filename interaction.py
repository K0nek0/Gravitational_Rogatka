import numpy as np
from scipy.integrate import odeint

G = 6.67 * 10**(-11)
ae = 149.6 * 10**9
m_c = 1.9885 * 10**30
x_c = 0
y_c = 0

T = 365
t_end = 2 * 24 * 3600 * 365
t = np.linspace(0, t_end, T+1)
k = 200

r = 15
w = 400
h = 300

class Interaction:
    def __init__(self, x0, vx0, y0, vy0):
        self.x0 = x0
        self.vx0 = vx0
        self.y0 = y0
        self.vy0 = vy0
        self.s0 = self.x0, self.vx0, self.y0, self.vy0

    def func(self, s, t):
        x, vx, y, vy = s

        dxdt = vx
        dvxdt = (-G * m_c * (x - x_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

        dydt = vy
        dvydt = (-G * m_c * (y - y_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

        return dxdt, dvxdt, dydt, dvydt

    def solve_func(self, i):
       
        sol = odeint(self.func, self.s0, (t[i], t[i+1]))

        self.x = sol[1, 0]
        self.y = sol[1, 2]
        self.vx = sol[1, 1]
        self.vy = sol[1, 3]

        self.s0 = self.x, self.vx, self.y, self.vy

        return self.x / ae, self.y / ae
