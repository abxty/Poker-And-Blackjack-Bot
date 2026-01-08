import sqlite3
import secrets
import hashlib
import hmac
from .databaseutils import getConnection, randomsalt, hash_algo


def convertselect(text, type):
    text = str(text)
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace(',', '')
    if type == "int":
        text = int(text)
    elif type == "non":
        text = text.replace("'", '')
    return text

def checklogin(username, password):
    """
    Checks for Login Details 

    Parameters:
    username (string): Username
    password (string): Password

    Returns:
    bool: Successfully Login
    string: simple message
    username: if successful return username
    """
    #connect = sqlite3.connect('C:/Users/samue/OneDrive/Desktop/casino venv/casino.db')
    connect = sqlite3.connect('casino.db')
    
    cursor = connect.cursor()
    cursor.execute(f"""SELECT salt FROM users WHERE username = '{username}';""")
    hashkey = cursor.fetchone()
    connect.commit()
    cursor.execute(f"""SELECT password FROM users WHERE username = '{username}';""")
    hashedpass = cursor.fetchone()
    connect.commit()
    hashkey = convertselect(hashkey, "non")
    hashedpass = convertselect(hashedpass, "non")

    if hash_algo(hashkey, password) == hashedpass:
        cursor.execute(f"""SELECT username FROM users WHERE username = '{username}' AND password = '{hashedpass}';""")
        connect.commit()
        # print("welcome", username)
        # loop = False
        cursor.close()
        connect.close()
        return True, "welcome", username
    else:
        #print("incorrect username or password!!!")
        return False, "incorrect username or password", ""
    
    


