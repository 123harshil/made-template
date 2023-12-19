#!/bin/bash

# Execute your data pipeline
# Replace this with the command or script that runs your data pipeline
# For example:
python trafficprediction.py

# Check if the database files exist
db_file_1="D:\project2\Traffic.db"
db_file_2="D:\project2\weather.db"

if [ -f "$db_file_1" ] && [ -f "$db_file_2" ]; then
  echo "Databases created successfully!"
else
  echo "databases not created."
