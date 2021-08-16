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

    # def func(self, s, t):
    #     x, vx, y, vy = s

    #     dxdt = vx
    #     dvxdt = (-G * m_c * (x - x_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

    #     dydt = vy
    #     dvydt = (-G * m_c * (y - y_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

    #     return dxdt, dvxdt, dydt, dvydt
        x_ar=[]
        vx_ar=[]
        y_ar=[]
        vy_ar=[]
        x_ar.append(x0)
        vx_ar.append(vx0)
        y_ar.append(y0)
        vy_ar.append(vy0)

        for i in range(t_end):
            x0 += T * vx0
            vx0 += T * (-G * m_c * (x0 - x_c) / ((x0 - x_c)**2 + (y0 - y_c)**2)**1.5)
            y0 += T * vy0
            vy0 += T * (-G * m_c * (y0 - y_c) / ((x0 - x_c)**2 + (y0 - y_c)**2)**1.5)
            x_ar.append(x0)
            vx_ar.append(vx0)
            y_ar.append(y0)
            vy_ar.append(vy0)
        return x_ar, vx_ar, y_ar, vy_ar


    def solve_func(self, i):
       
        # sol = odeint(self.func, self.s0, (t[i], t[i+1]))
        self.x = self.__init__()[0][i]
        self.vx = self.__init__()[1][i]
        self.y = self.__init__()[2][i]
        self.vy = self.__init__()[3][i]
        # self.x = sol[1, 0]
        # self.y = sol[1, 2]
        # self.vx = sol[1, 1]
        # self.vy = sol[1, 3]

        # self.s0 = self.x, self.vx, self.y, self.vy

        return self.x / ae, self.y / ae
