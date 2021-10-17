class Core:

    def checkPassword(self, app):
        self.password = "test"

        if self.password == app.LStxt.get():
            app.passwordVault()
        else:
            app.LStxt.delete(0, "end")
            app.LSlbl1.config(text="Неверный пароль")

    def savePassword(self, app):
        if app.FStxt.get() == app.FStxt1.get():
            pass
        else:
            app.FSlbl2.config(text="Пароли не совпадают")