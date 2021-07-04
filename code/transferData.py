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
    cursor.execute("CREATE TABLE IF NOT EXISTS corona_analysis (iso_code VARCHAR(50), continent VARCHAR(50), location VARCHAR(50), date DATE, total_cases INT(100) NULL, new_cases INT(100) NULL, total_deaths INT(100) NULL, new_deaths INT(100) NULL, icu_patients INT(100) NULL, new_tests INT(100) NULL, total_tests INT(100) NULL, positive_rate INT(100) NULL, total_vaccinations INT(100) NULL, people_vaccinated INT(100) NULL, people_fully_vaccinated INT(100) NULL, new_vaccinations INT(100) NULL, population INT(100) NULL);")
    end   = time.time()
    print(f'[✔] finished checking/creating!\ntime to create/check: {round(end-start, 2)} sec\n')
except:
    print('[💣] error while creating the table!')

#Inserting to the table
try:
    csv_data = csv.reader(open('../datasets/gulf.csv'))
    header = next(csv_data)
    print('[🔥] Inserting in Process ...!')
    for row in csv_data:
        print(row)
        cursor.execute(
            "INSERT INTO corona_analysis (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
except Exception as e:
    print(f'[!] error while inserting... \n{e}')

#Outputing the results
dbConnection.commit()
cursor.close()
dbConnection.close()
print('[✔] Process Done!')