import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    UNIQUE(email)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_settings(
    id bigint NOT NULL PRIMARY KEY,
    user_id bigint NOT NULL,
    settings json NOT NULL,

     CONSTRAINT FK_user_id FOREIGN KEY(user_id)
        REFERENCES users(user_id));

''')

cursor.execute('''
CREATE INDEX CONCURRENTLY IF NOT EXISTS users_name_key ON users(name);
''')

cursor.execute('''
CREATE INDEX CONCURRENTLY IF NOT EXISTS users_id_settings_key ON users_settings(user_id);
''')

cursor.execute('''
ALTER TABLE users_settings ADD COLUMN id BIGSERIAL PRIMARY KEY;
''')

cursor.execute('''
ALTER TABLE users_settings ADD CONSTRAINT constraint_name UNIQUE (user_id);
''')

connection.commit()
connection.close()