import hashlib
from tkinter import simpledialog

class Core:

    def popUp(self, text):
        self.answer = simpledialog.askstring("Менеджер паролей", text)
        return self.answer

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

    def addEntry(self, app, cursor, db):
        text1 = "Название сайта                                                         "
        text2 = "Логин                                                                      "
        text3 = "Пароль                                                                     "

        self.website = self.popUp(text1)
        self.username = self.popUp(text2)
        self.password = self.popUp(text3)

        insert_fields = """INSERT INTO vault(website,username,password)
        VALUES(?, ?, ?)"""
        cursor.execute(insert_fields, (self.website, self.username, self.password))
        db.commit()

        app.passwordVault()

    def removeEntry(self, input, app, cursor, db):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        app.passwordVault()

    def getMasterPassword(self, app, cursor):
        self.checkHashedPassword = self.hashPassword(app.LStxt.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(self.checkHashedPassword)])
        return cursor.fetchall()

    def hashPassword(self, input):
        self.hash = hashlib.md5(input)
        self.hash = self.hash.hexdigest()
        return self.hash