#!/bin/bash

# Execute your data pipeline
python project/trafficprediction.py  # Update this line with the correct relative path

# Check if the database files exist
db_file_1="D:/project2/Traffic.db"  # Update these paths with the correct database paths
db_file_2="D:/project2/weather.db"

if [ -f "$db_file_1" ] && [ -f "$db_file_2" ]; then
  echo "Databases created successfully!"
else
  echo "Error: Databases not created."
fi
