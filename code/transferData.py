try:
    import time
    import csv
    import pandas as pd
    import mysql.connector as conn
    from config import *
except Exception as e:
    print(f'error while importing packages!\n {e}')

#creating connection and configuration
dbConnection = conn.connect(**config)
#init the cursor
cursor = dbConnection.cursor()
#check if connection established!
print(f'[🔥] Connection ... \n{dbConnection}\n')

#creating database table
try:
    start = time.time()
    print('[🔥] checking if table exists or creating one ...')
    cursor.execute("CREATE TABLE IF NOT EXISTS corona_analysis (iso_code VARCHAR(50), continent VARCHAR(50), location VARCHAR(50), date DATE, total_cases INT(100), new_cases INT(100), total_deaths INT(100), new_deaths INT(100), icu_patients INT(100), new_tests INT(100), total_tests INT(100), positive_rate INT(100), total_vaccinations INT(100), people_vaccinated INT(100), people_fully_vaccinated INT(100), new_vaccinations INT(100), population INT(100));")
    end   = time.time()
    print(f'[✔️ ] finished checking/creating!\ntime to create/check: {round(end-start, 2)}\n')
except:
    print('[💣] error while creating the table!')

#Inserting to the table
csv_data = csv.reader(open('../datasets/owid-covid-data.csv'))
header = next(csv_data)
print('[🔥] Inserting in Process ...!')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona_analysis (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

#Outputing the results
dbConnection.commit()
cursor.close()
dbConnection.close()
print('[✔️] Process Done!')