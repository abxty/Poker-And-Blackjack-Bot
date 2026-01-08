import hashlib
import hmac
import secrets
import sqlite3

def getConnection():
    """
    Gets a central database connection
    """ 

    connect = sqlite3.connect('C:/database/casino.db')

    return connect

def randomsalt():
    """
    Generate a Random salt

    Returns:
    (bytes) Salted for password. 
    """
    salt = 256*3//4
    return secrets.token_urlsafe(salt)


def hash_algo(salt, password):
    """
     Takes a password and Salt 

    Parameters:
    salt (bytes): Username
    password (string): Password

    Returns:
    Hash password with using the salt. 
    """
    salt = bytes(salt, 'utf-8')
    password = bytes(password, 'utf-8')
    digest = hmac.new(salt, password, hashlib.sha256)
    return digest.hexdigest()