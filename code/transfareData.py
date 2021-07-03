try:
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
print(f'Connection ... \n{dbConnection}')

#Inserting to the table
csv_data = csv.reader(open('../datasets/owid-covid-data.csv'))
header = next(csv_data)
print('Inserting in Process ...!')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona_analysis (iso_code,continent,location,date,total_cases,new_cases,total_deaths,new_deaths,icu_patients,new_tests,total_tests,positive_rate,total_vaccinations,people_vaccinated,people_fully_vaccinated,new_vaccinations,population,median_age,aged_65_older,aged_70_older,female_smokers,male_smokers,human_development_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

#Outputing the results
dbConnection.commit()
cursor.close()
dbConnection.close()
print('Process Done!')