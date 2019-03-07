import random
from enum import Enum
import tkinter as tk
import threading
from time import sleep
from pynput import keyboard

cou = 0


class Direct(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    none = 4


class Color(object):
    def randcolor(self):
        r = int(random.randint(16, 255))
        g = int(random.randint(16, 200))
        b = int(random.randint(16, 145))

        return self.rgb2hex(r, g, b)

    def rgb2hex(self, r=255, g=255, b=255):
        r = hex(r)
        g = hex(g)
        b = hex(b)
        return '#' + self.check(str(r)[2:4]) + self.check(str(g)[2:4]) + self.check(str(b)[2:4])

    def check(self, r):
        if len(r) == 1:
            r = '0' + r
        return r


class Snake(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.length = 3
        self.point: list = [{'x': 200, 'y': 200}, {'x': 190, 'y': 200}, {'x': 180, 'y': 200}]
        self.root = root
        self.direct = Direct.right
        self.boom = False
        self.eat = 0

        self.root.geometry('400x400+400+50')
        main_frame = tk.Frame(self.root, height=400, width=400, bg='gray')
        main_frame.place(in_=self.root, y=30, x=0)

        self.cv = tk.Canvas(main_frame, bg='white', width=400, height=400)
        self.cv.place(in_=main_frame, x=0, y=0)
        self.redraw()

    def move_ball(self):
        print('move ball ', end='')
        # 算法 除头部外其余 坐标分别等于前一个的坐标   then 头部变化
        for i in range(self.length - 1, 0, -1):
            self.point[i]['x'], self.point[i]['y'] = self.point[i - 1]['x'], self.point[i - 1]['y']
        # 剔除 左右向时 向左右转向   上下向时 向上下转向
        if self.direct == Direct.right:
            self.point[0]['x'] += 10
            self.point[0]['x'] = self.point[0]['x'] % 390
        elif self.direct == Direct.left:
            self.point[0]['x'] -= 10
            self.point[0]['x'] = self.point[0]['x'] % 390
        elif self.direct == Direct.up:
            self.point[0]['y'] -= 10
            self.point[0]['y'] = self.point[0]['y'] % 370
        elif self.direct == Direct.down:
            self.point[0]['y'] += 10
            self.point[0]['y'] = self.point[0]['y'] % 370
        print(self.point)
        print('')
        if self.point[0] == self.point[-1]:
            self.length += 1
            global cou
            cou = 0
            LayEgg(self).lay()
            self.eat = 1

        for index in range(1, self.length - self.eat):
            if self.point[0]['x'] == self.point[index]['x'] and self.point[0]['y'] == self.point[index]['y']:
                self.boom = True

    def redraw(self):
        # 根据 坐标 重绘 蛇
        self.cv.delete('all')
        for p in self.point:
            self.cv.create_oval(p['x'] - 5, p['y'] - 5, p['x'] + 5, p['y'] + 5,
                                fill=Color().rgb2hex(230, p['y'] % 255, p['x'] % 160))
        self.cv.create_text((370, 20), text='X' + str(self.length))
        self.cv.create_oval(345, 15, 355, 25,
                            fill='pink')

    def run(self):
        while True:
            if self.boom:
                break
            self.redraw()
            sleep(0.1)


class SnakeThread(threading.Thread):
    def __init__(self, snake):
        threading.Thread.__init__(self)
        self.snake = snake

    def get_snake(self):
        return self.snake

    def run(self):
        global cou
        cou = 0
        while True:
            if self.snake.boom:
                cv = self.snake.cv
                cv.create_text((200, 200), text='GAME OVER')
                global ro
                ro = self.snake.root
                endbutton = tk.Button(ro,text='重新开始')
                endbutton.place(in_=ro, x=175, y=300)
                endbutton.bind('<Button-1>', lambda e:regame(root=ro))
                break

            if cou % 50 == 0:
                LayEgg(self.snake).lay()
            self.snake.move_ball()
            sleep(0.15)
            cou += 1


class KeyListenerThread(threading.Thread):
    def __init__(self, snake):
        threading.Thread.__init__(self)
        self.snake = snake

    def on_press(self, key):
        self.key = str(key)
        print(self.key)
        self.set_direct()

    def set_direct(self):
        if (
                self.key == '\'w\'' or self.key == '\'W\'' or self.key == 'Key.up') and self.snake.direct != Direct.up and self.snake.direct != Direct.down:
            print('{}pressed'.format(self.key))
            self.snake.direct = Direct.up
        elif (
                self.key == '\'a\'' or self.key == '\'A\'' or self.key == 'Key.left') and self.snake.direct != Direct.right and self.snake.direct != Direct.left:
            print('{}pressed'.format(self.key))
            self.snake.direct = Direct.left
        elif (
                self.key == '\'s\'' or self.key == '\'S\'' or self.key == 'Key.down') and self.snake.direct != Direct.up and self.snake.direct != Direct.down:
            print('{}pressed'.format(self.key))
            self.snake.direct = Direct.down
        elif (
                self.key == '\'d\'' or self.key == '\'D\'' or self.key == 'Key.right') and self.snake.direct != Direct.right and self.snake.direct != Direct.left:
            print('{}pressed'.format(self.key))
            self.snake.direct = Direct.right
        else:
            return

    def run(self):
        while True:
            with keyboard.Listener(
                    on_press=self.on_press)as listener:
                listener.join()


class LayEgg(object):
    def __init__(self, snake: Snake):
        self.snake = snake
        threading.Thread.__init__(self)

    def lay(self):
        repeat = True
        while repeat:
            x = int(random.randint(1, 39)) * 10
            y = int(random.randint(1, 37)) * 10
            for p in self.snake.point:
                if p['x'] == x and p['y'] == y:
                    repeat = True
                    break
            repeat = False
        if self.snake.length < self.snake.point.__len__():
            self.snake.point[self.snake.length] = {'x': x, 'y': y}
        else:
            self.snake.point.append({'x': x, 'y': y})
        self.snake.eat = 0

def game(r):
    SnakeT = Snake(r)
    st = SnakeThread(SnakeT)
    kt = KeyListenerThread(SnakeT)
    SnakeT.start()
    st.start()
    kt.start()
    r.mainloop()

def regame(**kw):
    prer = kw['root']
    print('happend',prer)
    r = tk.Tk()
    print('happend',r)
    SnakeT = Snake(r)
    st = SnakeThread(SnakeT)
    kt = KeyListenerThread(SnakeT)
    SnakeT.start()
    st.start()
    kt.start()
    r.mainloop()
    prer.destroy()


root = tk.Tk()
game(root)
