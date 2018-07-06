import sqlite3
import os

DBPATH  = 'database.db'
SQLPATH = 'database.sql'

def reset_database():
  try: 
    os.remove(DBPATH)
  except FileNotFoundError:
    pass
    
  conn = sqlite3.connect(DBPATH)
  cur = conn.cursor()
  script_file = open(SQLPATH, 'r')
  script = script_file.read()
  script_file.close()
  cur.executescript(script)
  conn.commit()
  conn.close()
  
reset_database()