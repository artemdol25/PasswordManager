from tkinter import *

class App:

    def __init__(self):
        self.window = Tk()
        self.window.title("Менеджер паролей")

        self.loginScreen()

        self.window.mainloop()

    def loginScreen(self):
        self.window.geometry("350x120")

        self.LSlbl = Label(self.window, text="Введите мастер-пароль")
        self.LSlbl.config(anchor=CENTER)
        self.LSlbl.pack()

        self.LStxt = Entry(self.window, width=20)
        self.LStxt.pack()

        self.LSbtn = Button(self.window, text="Войти")
        self.LSbtn.pack(pady=10)

        self.LSAuthor = Label(self.window, text="\u00a9 2021 Долгополов Артём")
        self.LSAuthor.pack(pady=2)

application = App()