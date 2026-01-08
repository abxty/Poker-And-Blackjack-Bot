import hashlib
import hmac
import secrets
import sqlite3
from .databaseutils import getConnection, randomsalt, hash_algo

def createuser(username, password):
    connect = sqlite3.connect('casino.db')
    cursor = connect.cursor()
    loop1 = True
    credits = 10000
    if len(username) == 0 or len(username) > 10:
        return False, "enter a valid username" 
    elif len(username) < 11:
        if len(password) > 7:                    
            for upper in password:
                if upper.isupper() == True:
                    loop1 = False
                    break
            if loop1 == True:
                return False, "Password must contain an uppercase letter"                    
        else:
            return False, "Password must be at least 7 characters"
    else:
        return False, "username is longer than 10 characters"

    try:
        salt = randomsalt()
        password = hash_algo(salt, password)
        cursor.execute("""INSERT INTO users (username, password, credits, salt) VALUES (?, ?, ?, ?)""",
                (username, password, credits, salt))                
        connect.commit()
        cursor.close()
        connect.close()
        return True, ""
    except:
        return False, "username already exists"
            