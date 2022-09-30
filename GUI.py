import tkinter

class TransPage:

    def __init__(self):
        page = tkinter.Tk()
        text = tkinter.Text(page)
        text.pack()

root = TransPage()
root.page.mainloop()