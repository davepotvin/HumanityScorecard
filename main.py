import sqlite3
import pandas as pd

def connect_db():
    return sqlite3.connect('humanity_scorecard.db')

# uncomment to delete table so the next chunk refresh
# conn = connect_db()
# conn.execute('DROP TABLE stats')

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            stats_id INTEGER PRIMARY KEY,
            year INTEGER,
            stat_type TEXT,
            stat_value REAL,
            source TEXT
        ) 
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    connect_db()
    create_table()
    
