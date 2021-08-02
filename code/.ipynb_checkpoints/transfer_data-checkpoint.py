import time,csv
import pandas as pd
import sqlite3 as conn
from etl_data import data

def db_connect():
    #creating connection, configuration and initializing the cursor
    global cursor, connect_db #making the cursor global for other functions
    connect_db  = conn.connect('./database/db/jobseekers.db',timeout=10) #connect to sqlite3 and create db if not exists with timeout=10 sec
    cursor = connect_db.cursor()
    #check if connection established!
    print(f'[🔥] Connecting to Database ... \n{connect_db}\
          \n[✔] Connected Successfully!\n')

def create_table():
    try:
        #creating database table and calc time of excution
        start_create = time.time()
        print('[🔥] Checking if table exists or creating one ...')
        tb_query = "CREATE TABLE IF NOT EXISTS jobseekers({})".format(' ,'.join(data.columns))
        cursor.execute(tb_query)
        end_create   = time.time()
        print(f'[✔] Finished creating Table: jobseekers!\nTime to create/check Table: {round(end_create-start_create, 2)} sec\n')
    
    except Exception as e:
        print(f'[!] Table: jobseekers exists so not created!\n{e}\n')

def create_unique_index():
    try:
        #creating database table and calc time of excution
        start_create = time.time()
        print('[🔥] Creating UNIQUE Index by Date ...')
        tb_index = "CREATE UNIQUE INDEX idx_jobseekers_id ON jobseekers (id)"
        cursor.execute(tb_index)
        end_create   = time.time()
        print(f'[✔] Finished Unique Index!\nTime to create/check Index: {round(end_create-start_create, 2)} sec\n')
    
    except Exception as e:
        print(f'[!] Index: error while making UNIQUE INDEX!\n{e}\n')

def insert_data():
    try:
        #Inserting to the table we inserted before!
        sql_insert = "REPLACE INTO jobseekers ({}) VALUES ({})".format(' ,'.join(data.columns), ','.join(['?']*len(data.columns)))
        print('\n[🔥] Inserting to Database Table in Process ...!')
        start_insert = time.time()

        for row in data.iterrows():
            start_insert_row = time.time()
            print(f'[🔥] Inserting Row Data ...\n{row}\n')
            cursor.execute(sql_insert, tuple(row[1]))
            end_insert_row = time.time()
            print(f'[✔] Finished inserting!\nTime to insert row data: {round(end_insert_row-start_insert_row, 2)} sec\n')

        end_insert  = time.time()
        print(f'[✔] Finished inserting all Data to the Database Table!\nTime to insert all data: {round(end_insert-start_insert, 2)} sec\n')
        print('[✔] Process Done!')
        
    except Exception as e:
        print(f'[!] Table: Cant Insert Data to the Table jobseekers!\n{e}\n')

    #Closing connection and commits
    connect_db.commit()
    cursor.close()
    connect_db.close()

#excuting all functions results!
db_connect(),create_table(),create_unique_index(),insert_data()
