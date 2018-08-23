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
        symbol = "AAPL"

        links = {
            "zacks": "https://www.zacks.com/stock/quote/{0}",
            "finvis": "https://finviz.com/quote.ashx?t={0}",
            "openinsider": "http://openinsider.com/search?q={0}",
            "earningswhispers": "https://earningswhispers.com/stocks/{0}",
            "shortsqueze":
                "http://shortsqueeze.com/?symbol={0}&submit=Short+Quote"
        }

        for link in links.values():
            wb.open(link.format(symbol))


root = tk.Tk()
app = Application(master=root)
app.mainloop()
