import interaction as i
import variables as var
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line
from kivy.uix.label import Label
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
# from kivy.uix.floatlayout import FloatLayout
from random import randint

# from kivy.config import Config
# Config.set('graphics', 'resizable', 0)
# Config.set('graphics', 'width', var.w)
# Config.set('graphics', 'height', var.h)

Builder.load_file('center.kv')

DRAG_START = ()
DRAG_END = ()
DRAGGING = False


class Object(Widget):
    def __init__(self, **kw):
        super(Object, self).__init__()
        self.step = kw['step']
        self.color = kw['color']
        self.pos = kw['pos']
        self.vel = kw['vel']
        self.COORDS = []

        self.interect = i.Interaction(x0=self.pos[0],
                                      vx0=self.vel[0],
                                      y0=self.pos[1],
                                      vy0=self.vel[1])

        for j in range(self.step):
            self.COORDS.append(
                (float(self.interect.solve_func(j)[0])*100+var.w,
                 float(self.interect.solve_func(j)[1])*100+var.h))

    def draw(self):
        self.canvas.add(self.color)
        self.ellipse = Ellipse(pos=self.pos, size=(var.r, var.r))
        self.canvas.add(self.ellipse)

    def move(self, c):
        self.pos = Vector(self.COORDS[c])
        self.ellipse.pos = self.pos


class Move(Widget):
    def __init__(self):
        super(Move, self).__init__()
        self.counter = 0
        self.n = var.t_end

    def update(self, dt):
        if self.counter == self.n - 1:
            self.counter = 0
        self.counter += 1
        self.object.move(self.counter)

    def create(self, color, pos, vel):
        self.object = Object(key=True,
                             color=color,
                             step=self.n,
                             pos=pos,
                             vel=vel)
        self.object.draw()
        self.add_widget(self.object)


class Painter(Widget):
    def __init__(self, **kw):
        super(Painter, self).__init__(**kw)
        Window.bind(mouse_pos=self.mouse_pos)

    def mouse_pos(self, window, pos):
        if DRAGGING == True:
            self.drawLine(pos)

    # отрисовка траектории
    def drawLine(self, mPos):
        # x и y векторы
        x_vector = self.x1 - mPos[0]
        y_vector = self.y1 - mPos[1]

        # модуль векторов
        vector_modul = (x_vector**2+y_vector**2)**(1/2)

        # расстояние от центра
        x_r = var.w - self.x1
        y_r = var.h - self.y1
        r_orbit = round(((x_r**2 + y_r**2)**0.5)/100, 1)

        try:
            cos_phi = x_vector/vector_modul
        except ZeroDivisionError:
            cos_phi = 0
        try:
            sin_phi = y_vector/vector_modul
        except ZeroDivisionError:
            sin_phi = 0

        v_modul = var.k*vector_modul

        # скорости
        self.vx = v_modul*cos_phi
        self.vy = v_modul*sin_phi

        self.canvas.after.clear()
        with self.canvas.after:
            self.label = Label(text=f'Скорость: {int(v_modul)} м/с',
                               pos=(self.x1, self.y1))
            self.label_center = Label(text=f'Расстояние до центра: {r_orbit} ae',
                               pos=(self.x1, self.y1-30))

        self.canvas.clear()
        with self.canvas:
            self.line = Line(points=[DRAG_START[0]+var.r/2, DRAG_START[1]+var.r/2, mPos[0], mPos[1]],
                             width=1.4)
            self.line_center = Line(points=[DRAG_START[0]+var.r/2, DRAG_START[1]+var.r/2, var.w, var.h],
                             width=1)

    def on_touch_down(self, touch):
        with self.canvas.before:
            self.color = Color(1, randint(0,1), randint(0,1), 1)
            self.ellipse = Ellipse(pos=(touch.x, touch.y), size=(var.r, var.r))

        self.x1 = touch.x
        self.y1 = touch.y

        global DRAGGING, DRAG_START
        DRAGGING = True
        DRAG_START = touch.pos

    def on_touch_up(self, touch):
        # убирание начальных элементов
        self.canvas.children.remove(self.line)
        self.canvas.children.remove(self.line_center)
        self.canvas.before.remove(self.ellipse)
        self.canvas.after.clear()

        # задание данных объекту
        self.object = Move()
        self.object.create(color=self.color,
                           pos=(((self.x1-var.w)/100)*var.ae, ((self.y1-var.h)/100)*var.ae),
                           vel=(self.vx, self.vy))
        Clock.schedule_interval(self.object.update, .04)
        self.parent.add_widget(self.object)

        global DRAGGING, DRAG_START
        DRAGGING = False

        # self.parent.remove_widget(self.object)

# class CustomLayout(FloatLayout):
#     pass

class PlanetApp(App):
    def build(self):
        return Painter()

if __name__ == '__main__':
    PlanetApp().run()

#self.center
