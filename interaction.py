# import numpy as np
# from scipy.integrate import odeint

G = 6.67 * 10**(-11)
ae = 149.6 * 10**9
m_c = 1.9885 * 10**30
x_c = 0
y_c = 0

T = 100
t_end = 1000
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
        # self.s0 = x0, vx0, y0, vy0

    # def func(self, s, t):
    #     x, vx, y, vy = s

    #     dxdt = vx
    #     dvxdt = (-G * m_c * (x - x_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

    #     dydt = vy
    #     dvydt = (-G * m_c * (y - y_c) / ((x - x_c)**2 + (y - y_c)**2)**1.5)

    #     return dxdt, dvxdt, dydt, dvydt

    def solver(self):
        x_ar=[]
        vx_ar=[]
        y_ar=[]
        vy_ar=[]
        x_ar.append(self.x0)
        vx_ar.append(self.vx0)
        y_ar.append(self.y0)
        vy_ar.append(self.vy0)
        print(x_ar)
        print(vx_ar)
        print(y_ar)
        print(vy_ar)

        for i in range(t_end):
            self.x0 += T * self.vx0
            self.vx0 += T * (-G * m_c * (self.x0 - x_c) / ((self.x0 - x_c)**2 + (self.y0 - y_c)**2)**1.5)
            self.y0 += T * self.vy0
            self.vy0 += T * (-G * m_c * (self.y0 - y_c) / ((self.x0 - x_c)**2 + (self.y0 - y_c)**2)**1.5)
            x_ar.append(self.x0)
            vx_ar.append(self.vx0)
            y_ar.append(self.y0)
            vy_ar.append(self.vy0)
        return x_ar, vx_ar, y_ar, vy_ar


    def solve_func(self, i):
       
        # sol = odeint(self.func, self.s0, (t[i], t[i+1]))
        self.x = self.solver()[0][i]
        self.vx = self.solver()[1][i]
        self.y = self.solver()[2][i]
        self.vy = self.solver()[3][i]
        # self.x = sol[1, 0]
        # self.y = sol[1, 2]
        # self.vx = sol[1, 1]
        # self.vy = sol[1, 3]

        # self.s0 = self.x, self.vx, self.y, self.vy
        return self.x / ae, self.y / ae
