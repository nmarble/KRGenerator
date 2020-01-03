from tkinter import *

class MainWindow(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("KR Generator")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Create New", command=self.onNew)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="Load", command=self.onLoad)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpMenu = Menu(menubar)
        helpMenu.add_command(label="Contributors", command=self.onExit)
        helpMenu.add_command(label="About", command=self.onExit)
        menubar.add_cascade(label="Help", menu=helpMenu)

    def onNew(self):

        self.quit()

    def onSave(self):

        self.quit()

    def onLoad(self):

        self.quit()

    def onExit(self):

        self.quit()

    def onCont(self):
        self.quit()

    def onAbout(self):
        self.quit()


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = MainWindow()
    root.mainloop()


if __name__ == '__main__':
    main()