import sqlite3

def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL
                    )''')
    
    connection.commit()
    connection.close()

# 初始化数据库
init_db()
