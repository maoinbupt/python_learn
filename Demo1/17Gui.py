from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        # pack()方法把Widget加入到父容器中，并实现布局
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

        #
        # self.nameInput = Entry(self)
        # self.nameInput.pack()
        #
        # self.alertButton = Button(self, text='Hello alert', command=self.hello())
        # self.alertButton.pack()



    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World title')
# 主消息循环:
app.mainloop()


