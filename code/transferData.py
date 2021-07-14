import time
import csv
import pandas as pd
import psycopg2 as conn
from configurations.PostgreSQL_Config import config

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

def CreateDB():
    #create new database and checks if exists and handle it
    try:
        startCreateDB = time.time()
        print('[🔥] Checking if database exists or creating new one ...')
        dbqueryCreate = "CREATE DATABASE coronadb;"
        cursor.execute(dbqueryCreate)
        endCreateDB   = time.time()
        print(f'[✔] Finished creating database: coronadb\nTime to create database: {round(endCreateDB-startCreateDB, 2)} sec\n')
    except:
        pass
        print(f'[✔] Database: coronadb Exists and Can Accessed!')

def TableInsertDB():
    #creating database table and calc time of excution
    startCreate = time.time()
    print('[🔥] Checking if table exists or creating one ...')
    dbquery = "CREATE TABLE IF NOT EXISTS ksadata (iso_code text, continent text, location text, dates date, total_cases real NULL, new_cases real NULL, total_deaths real NULL, new_deaths real NULL, icu_patients real NULL, new_tests real NULL, total_tests real NULL, positive_rate real NULL, total_vaccinations real NULL, people_vaccinated real NULL, people_fully_vaccinated real NULL, new_vaccinations real NULL, population real NULL, median_age real NULL, aged_65_older real NULL, aged_70_older real NULL, female_smokers real NULL, male_smokers real NULL, human_development_index real NULL);"
    cursor.execute(dbquery)
    endCreate   = time.time()
    print(f'[✔] Finished creating Table: ksadata!\nTime to create/check Table: {round(endCreate-startCreate, 2)} sec\n')

    #Inserting to the table we inserted before!
    csv_data = csv.reader(open('../datasets/created/ksa.csv'))
    print('[🔥] Inserting in Process ...!')
    startInsert = time.time()
    for row in csv_data:
        print(row)
        cursor.execute(
            "INSERT INTO ksadata (iso_code,continent,location,dates,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population,median_age,aged_65_older,aged_70_older,female_smokers,male_smokers,human_development_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
    endInsert  = time.time()
    print(f'[✔] Finished inserting!\nTime to insert all data: {round(endInsert-startInsert, 2)} sec\n')

    #Closing connection and commits
    DBconnect.commit()
    cursor.close()
    DBconnect.close()
    print('[✔] Process Done!')

#excuting all functions results!
DBConnect(),CreateDB(),TableInsertDB()
