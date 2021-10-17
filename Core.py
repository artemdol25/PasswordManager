import hashlib

class Core:

    def checkPassword(self, app, cursor):
        self.match = self.getMasterPassword(app, cursor)

        if self.match:
            app.passwordVault()
        else:
            app.LStxt.delete(0, "end")
            app.LSlbl1.config(text="Неверный пароль")

    def savePassword(self, app, cursor, db):
        if app.FStxt.get() == app.FStxt1.get():
            hashedPassword = self.hashPassword(app.FStxt.get().encode("utf-8"))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            app.passwordVault()
        else:
            app.FSlbl2.config(text="Пароли не совпадают")

    def getMasterPassword(self, app, cursor):
        self.checkHashedPassword = self.hashPassword(app.LStxt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(self.checkHashedPassword)])
        return cursor.fetchall()

    def hashPassword(self, input):
        self.hash = hashlib.md5(input)
        self.hash = self.hash.hexdigest()
        return self.hash