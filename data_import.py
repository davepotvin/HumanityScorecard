import sqlite3
import pandas as pd
from app import *

# taking a one big table approach here to keep things simple, no normalization

# tester function to go straight from mock data in csv into db, will remove once I've got real data
def insert_csv_data(csv_file):
    conn = connect_db()
    cur = conn.cursor()
    data = pd.read_csv(csv_file)
    
    for _, row in data.iterrows():
        cur.execute('''
            INSERT INTO stats (year, stat_type, stat_value, source)
            VALUES (?, ?, ?, ?)
        ''', (row['year'], row['stat_type'], row['stat_value'], row['source']))
    
    conn.commit()
    conn.close()
    
insert_csv_data('data/infant_mortality_rate.csv')

# helper function that will insert into db once data has been cleaned up
def insert_csv_data(df):
    conn = connect_db()
    cur = conn.cursor()
    
    for _, row in df.iterrows():
        cur.execute('''
            INSERT INTO stats (year, stat_type, stat_value, source)
            VALUES (?, ?, ?, ?)
        ''', (row['year'], row['stat_type'], row['stat_value'], row['source']))
    
    conn.commit()
    conn.close()

# need a cleaner function for each csv that will transform then insert the data
def process_infant_mortality(path_to_csv):
    df = pd.read_csv(path_to_csv)
    
    insert_csv_data(df)