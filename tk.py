import tkinter as tk
import webbrowser as wb


class Ticker(tk.Frame):
    links = {
        "zacks": "https://www.zacks.com/stock/quote/{0}",
        "finviz": "https://finviz.com/quote.ashx?t={0}",
        "openinsider": "http://openinsider.com/search?q={0}",
        "earningswhispers": "https://earningswhispers.com/stocks/{0}",
        "shortsqueeze": "http://shortsqueeze.com/?symbol={0}"
    }

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_buttons()
        self.create_text_box()

    def create_buttons(self):
        pass
        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Click here to open new tabs"
        # self.hi_there["command"] = self.openall
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

        self.text_box = tk.Entry(self)
        self.text_box.pack(side="bottom")
        self.text_box.bind('<Return>', self.run_search)
        self.text_box.focus()

    def run_search(self, event=None):
        symbol = self.text_box.get()
        self.text_box.delete(0, 'end')
        self.text_box.focus()

        for link in self.links.values():
            wb.open(link.format(symbol))


root = tk.Tk()
root.title('Ticker')
root.geometry("500x500")

app = Ticker(master=root)
app.mainloop()
