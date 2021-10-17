class Core:

    def checkPassword(self, app, cursor):
        match = self.getMasterPassword(app, cursor)


        if match:
            app.passwordVault()
        else:
            app.LStxt.delete(0, "end")
            app.LSlbl1.config(text="Неверный пароль")

    def savePassword(self, app, cursor, db):
        if app.FStxt.get() == app.FStxt1.get():
            hashedPassword = app.FStxt.get()

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            app.passwordVault()
        else:
            app.FSlbl2.config(text="Пароли не совпадают")

    def getMasterPassword(self, app, cursor):
        checkHashedPassword = app.LStxt.get()
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])
        return cursor.fetchall()