from tkinter import *
from functools import partial
from Core import Core

class App:

    def __init__(self):
        self.window = Tk()
        self.core = Core()
        self.window.title("Менеджер паролей")

        self.firstScreen()

        self.window.mainloop()

    def loginScreen(self):
        self.window.geometry("350x150")

        self.LSlbl = Label(self.window, text="Введите мастер-пароль")
        self.LSlbl.config(anchor=CENTER)
        self.LSlbl.pack()

        self.LStxt = Entry(self.window, width=20, show="*")
        self.LStxt.pack()
        self.LStxt.focus()

        self.LSlbl1 = Label(self.window)
        self.LSlbl1.pack()

        self.LSbtn = Button(self.window, text="Войти", command=partial(self.core.checkPassword, self))
        self.LSbtn.pack(pady=10)

        self.LSAuthor = Label(self.window, text="\u00a9 2021 Долгополов Артём")
        self.LSAuthor.pack(pady=2)

    def firstScreen(self):
        self.window.geometry("350x200")

        self.FSlbl = Label(self.window, text="Придумайте мастер-пароль")
        self.FSlbl.config(anchor=CENTER)
        self.FSlbl.pack()

        self.FStxt = Entry(self.window, width=20, show="*")
        self.FStxt.pack()
        self.FStxt.focus()

        self.FSlbl1 = Label(self.window, text="Повторите мастер-пароль")
        self.FSlbl1.pack()

        self.FStxt1 = Entry(self.window, width=20, show="*")
        self.FStxt1.pack()

        self.LSbtn = Button(self.window, text="Войти", command=partial(self.core.savePassword, self))
        self.LSbtn.pack(pady=10)

        self.FSlbl2 = Label(self.window)
        self.FSlbl2.pack()

        self.LSAuthor = Label(self.window, text="\u00a9 2021 Долгополов Артём")
        self.LSAuthor.pack(pady=5)

    def passwordVault(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.geometry("700x350")

        self.PVlblb = Label(self.window, text="Сохранённые пароли")
        self.PVlblb.config(anchor=CENTER)
        self.PVlblb.pack()

application = App()