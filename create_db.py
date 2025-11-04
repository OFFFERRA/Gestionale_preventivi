import sqlite3 as sq

#Create a new database from db.sql

conn = sq.connect('preventivi.sqlite3')

with open("db.sql") as f:
    conn.executescript(f.read())

conn.close()