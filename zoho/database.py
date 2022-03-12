from sqlite3 import *


class Database:
    def __init__(self) -> None:
        self.mydb = "mydb.db"
        with connect(self.mydb) as db:
            db.execute('''
                CREATE TABLE IF NOT EXISTS USERS(
                    EMAIL TEXT,
                    PASSWORD TEXT,
                    PRIMARY KEY(EMAIL)
                );
        ''')
        with connect(self.mydb) as db:
            db.execute('''
            CREATE TABLE IF NOT EXISTS CONTACT(
                PEMAIL TEXT,
                NAME TEXT,
                PHNO INTEGER,
                MAIL TEXT
            );
            ''')
    def signIn(self,email,password):
        with connect(self.mydb) as db:
            for i in db.execute("SELECT * FROM USERS WHERE EMAIL = ? AND PASSWORD = ?;",(email,password)):
                return i;
        return False

    def getData(self,email):
        with connect(self.mydb) as db:
            for i in db.execute("SELECT * FROM USERS WHERE EMAIL = ?;",(email,)):
                return i;
        return False;

    def signUp(self,email,password):
        if(self.getData(email) == False):
            with connect(self.mydb) as db:
                db.execute("INSERT INTO USERS(EMAIL,PASSWORD) VALUES(?,?);",(email,password));
                return True
        return False

    def saveContact(self,pemail,name,phno,email):
        try:
            with connect(self.mydb) as db:
                db.execute("INSERT INTO CONTACT(PEMAIL,NAME,PHNO,MAIL) VALUES(?,?,?,?);",(pemail,name,phno,email));
                return True
        except Exception as e:
            print(e)
            return False

    def getContacts(self,email):
        data = []
        try:
            with connect(self.mydb) as db:
                for i in db.execute("SELECT * FROM CONTACT WHERE PEMAIL = ?;",(email,)):
                    data.append(i)
            return data
        except Exception as e:
            print(e)
            return False;


print(Database().getContacts("mpraveen@gmail.com"))