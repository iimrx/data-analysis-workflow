import time
import csv
import pandas as pd
import mysql.connector as conn
from config import *

#creating connection and configuration
dbConnection = conn.connect(**config)
#init the cursor
cursor = dbConnection.cursor()
#check if connection established!
print(f'[🔥] Connection ... \n{dbConnection}\n')

def CreateInsertDB():
    #creating database table
    start = time.time()
    print('[🔥] checking if table exists or creating one ...')
    dbquery = "CREATE TABLE IF NOT EXISTS corona_analysis (iso_code VARCHAR(50), continent VARCHAR(50), location VARCHAR(50), date DATE, total_cases INT(100) NULL, new_cases INT(100) NULL, total_deaths INT(100) NULL, new_deaths INT(100) NULL, icu_patients INT(100) NULL, new_tests INT(100) NULL, total_tests INT(100) NULL, positive_rate DOUBLE(100) NULL, total_vaccinations INT(100) NULL, people_vaccinated INT(100) NULL, people_fully_vaccinated INT(100) NULL, new_vaccinations INT(100) NULL, population INT(100) NULL, median_age INT(100) NULL, aged_65_older INT(100) NULL, aged_70_older INT(100) NULL, female_smokers INT(100) NULL, male_smokers INT(100) NULL, human_development_index INT(100) NULL);"
    cursor.execute(dbquery)
    end   = time.time()
    print(f'[✔] finished checking/creating!\ntime to create/check: {round(end-start, 2)} sec\n')
    #Inserting to the table
    csv_data = csv.reader(open('../datasets/gulf.csv'))
    header = next(csv_data)
    print('[🔥] Inserting in Process ...!')
    for row in csv_data:
        print(row)
        cursor.execute(
            "INSERT INTO corona_analysis (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population,median_age,aged_65_older,aged_70_older,female_smokers,male_smokers,human_development_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

    #Outputing the results
    dbConnection.commit()
    cursor.close()
    dbConnection.close()
    print('[✔] Process Done!')

CreateInsertDB()