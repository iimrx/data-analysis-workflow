import time
import csv
import pandas as pd
import psycopg2 as conn
import PostgreSQL_Config as config

#creating connection and configuration
dbConnect = conn.connect(database=config.database, user=config.user,
                            password=config.password, host=config.host, port=config.port)
#init the cursor
cursor = dbConnect.cursor()
#check if connection established!
print(f'[🔥] Connection ... \n{dbConnect}\n\
      \n[✔] Connected Successfully!')

def CreateInsertDB():
    #creating database table
    start = time.time()
    print('[🔥] checking if table exists or creating one ...')
    dbquery = "CREATE TABLE IF NOT EXISTS corona_analysis (iso_code text, continent text, location text, date DATE, total_cases decimal NULL, new_cases decimal NULL, total_deaths decimal NULL, new_deaths decimal NULL, icu_patients decimal NULL, new_tests decimal NULL, total_tests decimal NULL, positive_rate real NULL, total_vaccinations decimal NULL, people_vaccinated decimal NULL, people_fully_vaccinated decimal NULL, new_vaccinations decimal NULL, population decimal NULL, median_age decimal NULL, aged_65_older decimal NULL, aged_70_older decimal NULL, female_smokers decimal NULL, male_smokers decimal NULL, human_development_index decimal NULL);"
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
    dbConnect.commit()
    cursor.close()
    dbConnect.close()
    print('[✔] Process Done!')

CreateInsertDB()