import pandas as pd
import sqlalchemy as db
import testConfig as cf
import mysql.connector as conn

# Create the engine to connect to the MySQL database,
engine = db.create_engine('mysql://cf.user:cf.password@34.87.39.39:3306/cf.database')
# Read data from SQL table
# we use read_sql_table to read the data using pandas commands
sql_data = pd.read_sql_table('sideProjectDB',engine)