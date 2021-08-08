#!/bin/bash

python3 ./code/etl_data.py #extraction, transformation and loading data
echo "Finished ETL Proccess ...!"
sleep 10
python3 ./code/transfer_data.py #importing the data to sqlite3 db
echo "Finished Importing To DB!"
sleep 10
#after we load the data to sqlite3 db, we converting it ti .sql file path to make it eaiser,
#for us to load it to multiple RDBs.
sqlite3 database/db/jobseekers.db .dump > database/sql/jobseekers.sql
echo "Finished Converting to SQL File.!"
