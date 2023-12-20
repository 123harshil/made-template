#!/bin/bash

# Install Python packages
pip install opendatasets
pip install pandas
pip install pysqlite3
pip install kaggle
pip install logging

python3 pipeline.py
python3 tests.py
