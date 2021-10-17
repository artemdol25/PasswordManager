import unittest
import sqlite3
from App import App
from Core import Core

with sqlite3.connect("Passwords.db") as db:
    cursor = db.cursor()

class TestCore(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.core = Core()

    def testpopUp(self):
        self.assertEqual(self.core.popUp("Название сайта"), "vk.ru")
        self.assertEqual(self.core.popUp("Логин"), "artemka")
        self.assertEqual(self.core.popUp("Пароль"), "228337")

        self.assertEqual(self.core.popUp("Название сайта"), "facebook.com")
        self.assertEqual(self.core.popUp("Логин"), "teman")
        self.assertEqual(self.core.popUp("Пароль"), "777")

        self.assertEqual(self.core.popUp("Название сайта"), "Google")
        self.assertEqual(self.core.popUp("Логин"), "tyoma@gmail.com")
        self.assertEqual(self.core.popUp("Пароль"), "biba")

    def testgetMasterPassword(self):
        cursor.execute("SELECT * FROM masterpassword")
        self.assertEqual(cursor.fetchall(), [(1, 'c8cfd2b5342a474eca08feabf3d2a11f')])

    def testPasswords(self):
        cursor.execute("SELECT * FROM vault")
        array = cursor.fetchall()
        self.assertEqual(array[0][1], 'vk.ru')
        self.assertEqual(array[1][2], 'teman')
        self.assertEqual(array[2][3], 'biba')
        self.assertEqual(array[0][3], '228337')
        self.assertEqual(array[1][1], 'facebook.com')
        self.assertEqual(array[2][2], 'tyoma@gmail.com')

    def testhashPassword(self):
        self.assertEqual(self.core.hashPassword('фкеуьлф'.encode('utf-8')), 'c8cfd2b5342a474eca08feabf3d2a11f')


if __name__ == "__main__":
    unittest.main()