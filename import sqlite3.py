import sqlite3

overallcreditpool = 123
username = "samuel"
connect = sqlite3.connect('C:/Users/samue/OneDrive/Desktop/casino venv/casino.db')
cursor = connect.cursor()

cursor.execute(f"""UPDATE users SET credits = '{overallcreditpool}' WHERE username = '{username}'""")