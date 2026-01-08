# from casinoproject.databaseutils import getConnection
import sqlite3

def showbalance(username):
    connect = sqlite3.connect('C:/database/casino.db')
    cursor = connect.cursor()
    cursor.execute(f"""SELECT credits, salt FROM users WHERE username = '{username}'""")
    row = cursor.fetchone()
    if row:
        credits = row[0]
        return credits
    else:
        return 0
