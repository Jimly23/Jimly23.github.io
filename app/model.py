import mysql.connector
import random

class DatabaseManager:
    def __init__(self) -> None:
        self.connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hardiansyah_23",
            database="seo"
        )
        self.cursor = self.connect.cursor()

    def sendMessage(self,username,email,subject,message):
        id = random.randint(1000,10000)

        insert = "INSERT INTO message(id,username,email,subject,message) VALUES(%s,%s,%s,%s,%s)"
        values = (id,username,email,subject,message)
        self.cursor.execute(insert,values)
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    def freeQuote(self,email,website):
        id = random.randint(1000,10000)
        
        insert = "INSERT INTO free_quote(id,email,website) VALUES(%s,%s,%s)"
        values = (id,email,website)
        self.cursor.execute(insert,values)
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

