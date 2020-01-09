import tkinter as tk


class MainWindow:

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.initUI()

    def initUI(self):
        self.parent.title("KR Generator")

        menubar = tk.Menu(self.frame)
        self.parent.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        fileMenu.add_command(label="Create New", command=self.onNew)
        fileMenu.add_command(label="Save", command=self.onSave)
        fileMenu.add_command(label="Load", command=self.onLoad)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        helpMenu = tk.Menu(menubar)
        helpMenu.add_command(label="Contributors", command=self.onExit)
        helpMenu.add_command(label="About", command=self.onExit)
        menubar.add_cascade(label="Help", menu=helpMenu)

    def onNew(self):
        self.newWindow = tk.Toplevel(self.parent)
        self.app = NewWindow(self.newWindow)

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


class NewWindow:

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, pady=3)

        self.mapNameLabel = tk.Label(self.frame, text='Map Name: ')
        self.mapNameLabel.pack()
        self.mapName = tk.Entry(self.frame)
        self.mapName.pack()

        self.mapXLabel = tk.Label(self.frame, text='Map X Size: ', width=25)
        self.mapXLabel.pack()
        self.mapXInput = tk.Spinbox(self.frame, width=25, from_=0, to=100)
        self.mapXInput.pack()

        self.mapYLabel = tk.Label(self.frame, text='Map Y Size: ')
        self.mapYLabel.pack()
        self.mapYInput = tk.Spinbox(self.frame, width=25, from_=0, to=100)
        self.mapYInput.pack()

        self.createButton = tk.Button(self.frame, text='Create', width=24, command=self.onCreate)
        self.createButton.pack()
        self.frame.pack()

    def onCreate(self):
        self.quit()

def main():
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
