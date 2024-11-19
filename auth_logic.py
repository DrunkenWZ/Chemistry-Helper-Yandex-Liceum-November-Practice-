import sqlite3

# Создаем базу данных и таблицу пользователей
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username, password):
    print(f"Попытка добавить пользователя: {username}")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Ошибка: пользователь {username} уже существует.") 
        return False  # Возвращаем False, если пользователь уже существует
    finally:
        conn.close()

def check_user(username, password):
    # Проверьте, корректно ли вы проверяете пользователя и пароль
    # Например, если используете SQLite:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None
