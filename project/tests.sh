#!/bin/bash

# Execute your data pipeline (pipeline.sh)
python /project/databasetest.py

# Validate the existence of output files
if [ -f "/data/Traffic.db" ] && [ -f "/data/weather.db" ]; then
    echo "Output files 'Traffic.db' and 'weather.db' exist."
    exit 0  # Exit with code 0 to indicate success
else
    echo "Error: Output files not found."
    exit 1  # Exit with non-zero code to indicate test failure
fi
