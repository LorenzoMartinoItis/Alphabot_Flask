import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

def verifica_utente(username, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    
    result = cur.fetchone()
    conn.close()
    
    if result and result[1]==username and result[2]==password:
        return True
    return False
    

def aggiungi_utente(username, password):
    
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    
    cur.execute('INSERT INTO users(username, password) VALUES(?,?)', (username, password))
    
    conn.commit()
    conn.close()
    
    return True