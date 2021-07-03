try:
	from testConfig import *
	import mysql.connector as conn
	from mysql.connector import errorcode
except Exception as e:
    print(f'error while importing packages!\n {e}')

#creating connection and configuration
dbConnection = conn.connect(**config)
#init the cursor
cursor = dbConnection.cursor()
#check if connection established!
print(f'Connection ... \n{dbConnection}')

#creating database table
TABLES = {}
TABLES['corona_analysis'] = (
    "CREATE TABLE `corona_analysis` ("
    "  `iso_code` varchar(50) NOT NULL,"
    "  `continent` varchar(50) NOT NULL,"
    "  `location` varchar(50) NOT NULL,"
    "  `date` date NOT NULL,"
    "  `total_cases` int('100') NOT NULL AUTO_INCREMENT,"
    "  `new_cases` int(100) NOT NULL AUTO_INCREMENT,"
    "  `total_deaths` int(100) NOT NULL AUTO_INCREMENT,"
    "  `new_deaths` int(100) NOT NULL AUTO_INCREMENT,"
    "  `icu_patients` int(100) NOT NULL AUTO_INCREMENT,"
    "  `new_tests` int(100) NOT NULL AUTO_INCREMENT,"
    "  `total_tests` int(100) NOT NULL AUTO_INCREMENT,"
    "  `positive_rate` int(100) NOT NULL AUTO_INCREMENT,"
    "  `total_vaccinations` int(100) NOT NULL AUTO_INCREMENT,"
    "  `people_vaccinated` int(100) NOT NULL AUTO_INCREMENT,"
    "  `people_fully_vaccinated` int(100) NOT NULL AUTO_INCREMENT,"
    "  `new_vaccinations` int(100) NOT NULL AUTO_INCREMENT,"
    "  `median_age` int(100) NOT NULL AUTO_INCREMENT,"
    "  `aged_65_older` int(100) NOT NULL AUTO_INCREMENT,"
    "  `aged_70_older` int(100) NOT NULL AUTO_INCREMENT,"
    "  `female_smokers` int(100) NOT NULL AUTO_INCREMENT,"
    "  `male_smokers` int(100) NOT NULL AUTO_INCREMENT,"
    "  `human_development_index` int(100) NOT NULL AUTO_INCREMENT,"
    "  PRIMARY KEY (`iso_code`)"
    ") ENGINE=InnoDB")

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except conn.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
dbConnection.close()