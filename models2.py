import sqlite3
from flask import Flask, g

db_location = 'bookings.db'

    
# create the tables 
def create_table():
    con = sqlite3.connect(db_location)
    cur = con.cursor()
# for the bookings
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        booking_date TEXT NOT NULL,
        time TEXT NOT NULL,
        table_num INTEGER NOT NULL
    );
    """)
# and for the simulated login
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """)

    # add the admin user 
    # create_admin()
    
    # End the connection
    con.close()
    
def create_admin():
    con = sqlite3.connect(db_location)
    cur = con.cursor()
    # Hardcoded admin credentials for demonstration
    user = 'Admin'
    password = 'password'
    cur = con.cursor()
    cur.execute("INSERT INTO admin (user, password) VALUES (?, ?)", (user, password))
    con.commit()

# Execute the create table function
create_table()
