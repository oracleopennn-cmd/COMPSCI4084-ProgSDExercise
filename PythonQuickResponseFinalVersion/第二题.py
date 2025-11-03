# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 12:19:28 2025

@author: WYK
"""

import sqlite3 as sql
conn = sql.Connection('Sales.db')
cursor = conn.cursor()
#初始化数据
def init_data():
    cursor.execute('''CREATE TABLE Sales(
        Date TEXT,
        Product TEXT,
        Quantity INTEGER,
        Price REAL,
        Total REAL,
        Date_Original TEXT,
        Month TEXT
        )''')
    data = [('2023-01-01','Chocolate',5,10.0,50.0,'2023-01-01','2023-01'),
            ('2023-01-02','Biscuits',7,205.0,140.0,'2023-01-02','2023-01'),
            ('2023-01-03','Sweets',9,15.0,135.0,'2023-01-03','2023-01'),
            ('2023-01-04','Water',3,7.5,22.5,'2023-01-03','2023-01'),
            ('2023-01-05','Orange Juice',8,12.5,100.0,'2023-01-04','2023-01')]
    cursor.executemany('''INSERT INTO Sales VALUES(?,?,?,?,?,?,?)''',data)
    conn.commit()
#看表（调试用
def view_table(name):
    query = f"SELECT * FROM {name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def cal_total():
    cursor.execute('SELECT SUM(Total) FROM Sales ')
    total = cursor.fetchone()[0]
    print(total)
def summary():
    cursor.execute('''
                   SELECT Product, SUM(Quantity) AS Total_Quantity
                   FROM Sales
                   WHERE strftime('%Y', Date) = '2023'
                   GROUP BY Product
                   ORDER BY Total_Quantity DESC
                   ''')
    results = cursor.fetchall()
    for product, qty in results:
        print(f"Product: {product}, Total Quantity Sold: {qty}")
#cursor.execute('DROP TABLE Sales')
#init_data()
#view_table("Sales")
cal_total()
summary()
conn.close()