import time
import csv
import pandas as pd
import psycopg2 as conn
from configurations.PostgreSQL_Config import config

def UserInput():
    #declaring user information
    print('[🔥] Getting User Details ...')
    #making the (DBname,DBtable,DBuser,DBpass) global for other functions
    global DBname,DBtable,DBuser,DBpass
    DBname = input("Enter New Database Name: ")
    DBtable= input("Enter New Table Name: ")
    DBuser = input("Enter New Username: ")
    DBpass = input("Enter New User Password: ")
    print('[✔] All Details Stored Successfully!\n')

def DBConnect():
    #creating connection, configuration and initializing the cursor
    global cursor, DBconnect #making the cursor global for other functions
    DBconnect  = conn.connect(**config)
    autocommit = conn.extensions.ISOLATION_LEVEL_AUTOCOMMIT
    DBconnect.set_isolation_level(autocommit)
    cursor = DBconnect.cursor()
    #check if connection established!
    print(f'[🔥] Connecting to Database ... \n{DBconnect}\
          \n[✔] Connected Successfully!\n')

def CreateDBUser():
    #create new database user if exists and check for it
    try:
        startCreateDBUser = time.time()
        print('\n[🔥] Creating New database user ...')
        dbqueryCreateUser = "CREATE USER {} WITH PASSWORD '{}';".format(DBuser,DBpass)
        dbqueryGrantUser  = "GRANT ALL PRIVILEGES ON DATABASE {} TO {};".format(DBname,DBuser)
        cursor.execute(dbqueryCreateUser, dbqueryGrantUser)
        endCreateDBUser   = time.time()
        print(f'[✔] Finished creating database user: {DBuser}!\nTime to create database user: {round(endCreateDBUser-startCreateDBUser, 2)} sec\n')
    except:
        pass
        print(f'[✔] User: {DBuser} Exists and Have All Privileges!')

def CreateDB():
    #create new database and checks if exists and handle it
    try:
        startCreateDB = time.time()
        print('[🔥] Checking if database exists or creating new one ...')
        dbqueryCreate = "CREATE DATABASE {};".format(DBname)
        cursor.execute(dbqueryCreate)
        endCreateDB   = time.time()
        print(f'[✔] Finished creating database: {DBname}\nTime to create database: {round(endCreateDB-startCreateDB, 2)} sec\n')
    except:
        pass
        print(f'[✔] Database: {DBname} Exists and Can Accessed!')

def TableInsertDB():
    #creating database table and calc time of excution
    startCreate = time.time()
    print('[🔥] Checking if table exists or creating one ...')
    dbquery = "CREATE TABLE IF NOT EXISTS {} (iso_code text, continent text, location text, date date, total_cases decimal NULL, new_cases decimal NULL, total_deaths decimal NULL, new_deaths decimal NULL, icu_patients decimal NULL, new_tests decimal NULL, total_tests decimal NULL, positive_rate real NULL, total_vaccinations decimal NULL, people_vaccinated decimal NULL, people_fully_vaccinated decimal NULL, new_vaccinations decimal NULL, population decimal NULL, median_age decimal NULL, aged_65_older decimal NULL, aged_70_older decimal NULL, female_smokers decimal NULL, male_smokers decimal NULL, human_development_index decimal NULL);".format(DBtable)
    cursor.execute(dbquery)
    endCreate   = time.time()
    print(f'[✔] Finished creating Table: {DBtable}!\nTime to create/check Table: {round(endCreate-startCreate, 2)} sec\n')

    #Inserting to the table we inserted before!
    csv_data = csv.reader(open('./datasets/created/ksa.csv'))
    print('[🔥] Inserting in Process ...!')
    startInsert = time.time()
    for row in csv_data:
        print(row)
        cursor.execute(
            "INSERT INTO {} (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population,median_age,aged_65_older,aged_70_older,female_smokers,male_smokers,human_development_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(DBtable), row)
    endInsert  = time.time()
    print(f'[✔] Finished inserting!\nTime to insert all data: {round(endInsert-startInsert, 2)} sec\n')

    #Closing connection and commits
    DBconnect.commit()
    cursor.close()
    DBconnect.close()
    print('[✔] Process Done!')

#excuting all functions results!
UserInput(),DBConnect(),CreateDBUser(),CreateDB(),TableInsertDB()
