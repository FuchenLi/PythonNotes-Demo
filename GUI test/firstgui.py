from tkinter import *
from tkinter import messagebox


class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()

        self.helloLabel = Label(self,text='Hello World!')
        self.helloLabel.pack()

        self.quitButton = Button(self, text='Quit',command=self.quit)
        self.quitButton.pack()

        self.helloButton = Button(self, text='Hello', command=self.hello)
        self.helloButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)


app = App()
app.master.title('My First Python GUI')
app.mainloop()

root = Tk()
root.mainloop()
