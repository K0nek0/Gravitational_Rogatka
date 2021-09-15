import variables as var

class Interaction:
    def __init__(self, x0, vx0, y0, vy0):
        self.x0 = x0
        self.vx0 = vx0
        self.y0 = y0
        self.vy0 = vy0

    def solver(self):
        x_ar=[] 
        vx_ar=[]
        y_ar=[]
        vy_ar=[]
        x_ar.append(self.x0)
        vx_ar.append(self.vx0)
        y_ar.append(self.y0)
        vy_ar.append(self.vy0)

        for i in range(var.t_end):
            self.x0 += var.T * self.vx0
            self.vx0 += var.T * (-var.G * var.m_c * (self.x0 - var.x_c) / ((self.x0 - var.x_c)**2 + (self.y0 - var.y_c)**2)**1.5)

            self.y0 += var.T * self.vy0
            self.vy0 += var.T * (-var.G * var.m_c * (self.y0 - var.y_c) / ((self.x0 - var.x_c)**2 + (self.y0 - var.y_c)**2)**1.5)

            x_ar.append(self.x0)
            vx_ar.append(self.vx0)
            y_ar.append(self.y0)
            vy_ar.append(self.vy0)

        return x_ar, vx_ar, y_ar, vy_ar


    def solve_func(self, i):
        self.x = self.solver()[0][i]
        self.vx = self.solver()[1][i]
        self.y = self.solver()[2][i]
        self.vy = self.solver()[3][i]

        return self.x / var.ae, self.y / var.ae
