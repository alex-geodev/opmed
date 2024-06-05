# https://docs.python.org/3/library/sqlite3.html

import sqlite3

connection = sqlite3.connect("ninelines.db")

def insert(query):
  cursor = connection.cursor()
  cursor.execute(query)
  connection.commit()
