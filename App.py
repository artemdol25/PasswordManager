import sqlite3
from tkinter import *
from functools import partial
from Core import Core

with sqlite3.connect("Passwords.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

class App:

    def __init__(self):
        self.window = Tk()
        self.core = Core()
        self.window.title("Менеджер паролей")

        cursor.execute("SELECT * from masterpassword")

        if cursor.fetchall():
            self.loginScreen()
        else:
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

        self.LSbtn = Button(self.window, text="Войти", command=partial(self.core.checkPassword, self, cursor))
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

        self.LSbtn = Button(self.window, text="Войти", command=partial(self.core.savePassword, self, cursor, db))
        self.LSbtn.pack(pady=10)

        self.FSlbl2 = Label(self.window)
        self.FSlbl2.pack()

        self.LSAuthor = Label(self.window, text="\u00a9 2021 Долгополов Артём")
        self.LSAuthor.pack(pady=5)

    def passwordVault(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.geometry("700x350")

        self.PVlbl = Label(self.window, text="Сохранённые пароли")
        self.PVlbl.grid(column=1)

        self.PVbtn = Button(self.window, text="+", command=partial(self.core.addEntry, self, cursor, db))
        self.PVbtn.grid(column=1, pady=10)

        self.PVlbl = Label(self.window, text="Сайт")
        self.PVlbl.grid(row=2, column=0, padx=80)
        self.PVlbl = Label(self.window, text="Логин")
        self.PVlbl.grid(row=2, column=1, padx=80)
        self.PVlbl = Label(self.window, text="Пароль")
        self.PVlbl.grid(row=2, column=2, padx=80)

        cursor.execute("SELECT * from vault")
        if (cursor.fetchall() != None):
            i = 0
            while True:
                cursor.execute("SELECT * FROM vault")
                array = cursor.fetchall()

                self.PVlbl1 = Label(self.window, text=(array[i][1]), font=("Helvetica, 12"))
                self.PVlbl1.grid(column=0, row=i+3)
                self.PVlbl1 = Label(self.window, text=(array[i][2]), font=("Helvetica, 12"))
                self.PVlbl1.grid(column=1, row=i+3)
                self.PVlbl1 = Label(self.window, text=(array[i][3]), font=("Helvetica, 12"))
                self.PVlbl1.grid(column=2, row=i+3)

                self.PVbtn = Button(self.window, text="Удалить", command=partial(self.core.removeEntry, array[i][0], self, cursor, db))
                self.PVbtn.grid(column=3, row=i+3, pady=10)

                i = i + 1

                cursor.execute("SELECT * FROM vault")
                if (len(cursor.fetchall()) <= 1):
                    break

application = App()