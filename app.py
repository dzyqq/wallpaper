# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# # 初始化数据库
# def init_db():
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT UNIQUE NOT NULL,
#                         password TEXT NOT NULL)''')
#     conn.commit()
#     conn.close()

# # 注册页面
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # 插入数据到数据库
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         try:
#             cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#             conn.commit()
#             return redirect(url_for('/login'))  # 注册成功后跳转到登录页面
#         except sqlite3.IntegrityError:
#             return 'Username already exists!'
#         finally:
#             conn.close()
#     return render_template('MyWallpaperLibrary.html')

# # 登录页面
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         # 查询用户数据
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#         user = cursor.fetchone()
#         conn.close()
#         if user:
#             return  render_template('Wallparper.html')
        
#         else:
#             return 'Invalid username or password.'
#     return render_template('Wallparper.html.html')

# if __name__ == '__main__':
#     init_db()  # 初始化数据库
#     app.run(debug=True)
#     from waitress import serve

# if __name__ == "__main__":
#     serve(app, host='127.0.0.1', port=5050)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# 初始化数据库
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 插入数据到数据库
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            return redirect(url_for('login'))  # 注册成功后跳转到登录页面
        except sqlite3.IntegrityError:
            return 'Username already exists!'
        finally:
            conn.close()
    return render_template('Wallpaper.html')

# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 查询用户数据
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return  render_template('MyWallpaperLibrary.html')
        
        else:
            return 'Invalid username or password.'
    return render_template('Wallpaper.html')

if __name__ == '__main__':
    init_db()  # 初始化数据库
    app.run(debug=True)
    from waitress import serve

if __name__ == "__main__":
    serve(app, host='https://mywallpaperlibrary.us.kg/', port=5000)


