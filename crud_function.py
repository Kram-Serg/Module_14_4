import os
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()

# def add_product():
#
#     producte1 = ['SLIM FORMULA', 'Ускоряет расщепление жира,снижает аппетит', 1200]
#     producte2 = ['OMEGA-3 75%', 'Биологически активная добавка к пище "Омеrа-3 75%"', 1600]
#     producte3 = ['Detox', 'Комплекс для очищения печени', 2200]
#     producte4 = ['MAGNESIUM SALT EPSON', 'Английская магниевая соль для принятия ванны', 800]
#
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte1)
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte2)
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte3)
#     cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', producte4)
#
#     connection.commit()

def get_all_products():
    product = cursor.execute('SELECT title, description, price FROM Products').fetchall()
    connection.commit()
    return product



initiate_db()
# add_product()
