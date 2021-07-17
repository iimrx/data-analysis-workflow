import time,csv
import pandas as pd
import sqlite3 as conn
from ETL import *

def DBConnect():
    #creating connection, configuration and initializing the cursor
    global cursor, DBconnection #making the cursor global for other functions
    DBconnection  = conn.connect('./database/coronadb.db',timeout=10) #connect to sqlite3 and create db if not exists with timeout=10 sec
    cursor = DBconnection.cursor()
    #check if connection established!
    print(f'[🔥] Connecting to Database ... \n{DBconnection}\
          \n[✔] Connected Successfully!\n')

def CreateTable():
    try:
        #creating database table and calc time of excution
        startCreate = time.time()
        print('[🔥] Checking if table exists or creating one ...')
        TBquery = "CREATE TABLE IF NOT EXISTS coviddata({})".format(' ,'.join(data.columns))
        cursor.execute(TBquery)
        endCreate   = time.time()
        print(f'[✔] Finished creating Table: coviddata!\nTime to create/check Table: {round(endCreate-startCreate, 2)} sec\n')
    
    except:
        pass
        print('[!] Table: coviddata exists so not created!\n')

def CreateUniqueIndex():
    try:
        #creating database table and calc time of excution
        startCreate = time.time()
        print('[🔥] Creating UNIQUE Index by Date ...')
        TBquery = "CREATE UNIQUE INDEX idx_coviddata_date ON coviddata (date)"
        cursor.execute(TBquery)
        endCreate   = time.time()
        print(f'[✔] Finished Unique Index!\nTime to create/check Index: {round(endCreate-startCreate, 2)} sec\n')
    
    except Exception as e:
        pass
        print('[!] Index: error while making UNIQUE INDEX!')
        print(e)

def InsertData():
    try:
        #Inserting to the table we inserted before!
        sqlInsert = "REPLACE INTO coviddata ({}) VALUES ({})".format(' ,'.join(data.columns), ','.join(['?']*len(data.columns)))
        print('\n[🔥] Inserting to Database Table in Process ...!')
        startInsert = time.time()

        for row in data.iterrows():
            startInsertRow = time.time()
            print(f'[🔥] Inserting Row Data ...\n{row}\n')
            cursor.execute(sqlInsert, tuple(row[1]))
            endInsertRow = time.time()
            print(f'[✔] Finished inserting!\nTime to insert row data: {round(endInsertRow-startInsertRow, 2)} sec\n')

        endInsert  = time.time()
        print(f'[✔] Finished inserting all Data to the Database Table!\nTime to insert all data: {round(endInsert-startInsert, 2)} sec\n')
        print('[✔] Process Done!')
        
    except Exception as e:
        pass
        print('[!] Table: Cant Insert Data to the Table covidtest!\n')
        print(e)

    #Closing connection and commits
    DBconnection.commit()
    cursor.close()
    DBconnection.close()

#excuting all functions results!
DBConnect(),CreateTable(),CreateUniqueIndex(),InsertData()
