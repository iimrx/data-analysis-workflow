#!/bin/bash

python3 ./code/etl_data.py #extraction, transformation and loading data
python3 ./code/transfer_data.py #importing the data to sqlite3 db
#after we load the data to sqlite3 db, we converting it ti .sql file path to make it eaiser,
#for us to load it to multiple RDBs.
sqlite3 database/db/coronadb.db .dump > database/sql/coronadb.sql
