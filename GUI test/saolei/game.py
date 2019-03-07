import random
import tkinter as tk


class Game(tk.Frame):
    def run(self):
        pass

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.table = self.make_table()
        self.count = 0
        fm = tk.Frame(master, width=198, height=198)
        fm.place(in_=master, x=0, y=30)
        self.fm = fm
        button_dict = dict()
        for i in range(0, 9):
            for j in range(0, 9):
                btn = tk.Button(fm, width=22, height=22)
                btn.place(in_=fm, x=i * 22, y=j * 22)
                button_dict[str(i) + str(j)] = btn
                btn.bind('<Button-1>', click_adapter(click, str(i) + str(j), self))
        self.btn_dict = button_dict

    def make_table(self):
        table = []
        for i in range(0, 9):
            temp = []
            for j in range(0, 9):
                temp.append(0)
            table.append(temp)
        boom = self.pop_boom()
        for i in range(0, 9):
            table[boom[i][0]][boom[i][1]] += 1
        temp_t = list()
        for i in range(0, 9):
            temp = []
            for j in range(0, 9):
                temp.append(0)
            temp_t.append(temp)

        for i in range(0, 9):
            for j in range(0, 9):
                if (i, j) in boom:
                    temp_t[i][j] = '*'
                    continue
                temp_num = table[i][j]
                if i - 1 >= 0:
                    temp_num += table[i - 1][j]
                    if j - 1 >= 0:
                        temp_num += table[i - 1][j - 1]
                    if j + 1 <= 8:
                        temp_num += table[i - 1][j + 1]
                if i + 1 <= 8:
                    temp_num += table[i + 1][j]
                    if j - 1 >= 0:
                        temp_num += table[i + 1][j - 1]
                    if j + 1 <= 8:
                        temp_num += table[i + 1][j + 1]
                temp_num += 0
                if j - 1 >= 0:
                    temp_num += table[i][j - 1]
                if j + 1 <= 8:
                    temp_num += table[i][j + 1]
                temp_t[i][j] = temp_num
        for i in temp_t:
            print(i)

        return temp_t

    def pop_boom(self):
        boom = list()
        while len(boom) != 10:
            x = int(random.randint(0, 8))
            y = int(random.randint(0, 8))
            if (x, y) in boom:
                continue
            else:
                boom.append((x, y))
        print(boom)
        return boom

    def show_back(self, x: int, y: int):
        print('do show_back|||{},{}'.format(x,y))
        isgoon = int(random.randint(0, 2))
        self.count += 1

        lab = tk.Label(self.fm,
                       width=20,
                       height=20,
                       text=str(self.table[x][y]),
                       bitmap='gray12',
                       compound='center')
        lab.place(in_=self.fm, x=x * 22, y=y * 22)
        # self.btn_dict[str(x)+str(y)].place_forget()

        if self.count >= 12:
            return
        if isgoon == 0 or isgoon == 1:
            return



        if x - 1 >= 0:
            self.show_back(x - 1, y)
        if x + 1 <= 8:
            self.show_back(x + 1, y)
        if y - 1 >= 0:
            self.show_back(x, y - 1)
        if y + 1 <= 8:
            self.show_back(x, y + 1)


def click_adapter(fun, *args):
    l = args[0]
    obj = args[1]
    return lambda event, fun=fun, l=l, obj=obj: fun(event, l, obj)


def click(e, l, obj: Game):
    print('点击坐标', l)
    startx = int(l[0])
    starty = int(l[1])

    if obj.table[startx][starty] == '*':
        obj.root.destroy()
    else:
        obj.count = 0
        obj.show_back(startx, starty)


root = tk.Tk()
root.title('扫雷')
root.geometry('198x228+400+50')
root.maxsize(300, 330)
t = Game(root)
t.mainloop()
