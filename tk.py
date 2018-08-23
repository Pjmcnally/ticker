import tkinter as tk
import webbrowser as wb


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Click here to open new tabs"
        self.hi_there["command"] = self.openall
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def openall(self):
        wb.open('https://www.google.com')
        wb.open('https://www.gmail.com')
        wb.open('https://maps.google.com')
        wb.open('https://drive.google.com/drive/my-drive')


root = tk.Tk()
app = Application(master=root)
app.mainloop()
