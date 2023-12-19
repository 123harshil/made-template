#!/bin/bash

# Check if traffic.db exists
if [ -f "data/Traffic.db" ]; then
  echo "traffic.db exists"
else
  echo "traffic.db does not exist"
  exit 1  # Exit with non-zero code to indicate test failure
fi

# Check if weather.db exists
if [ -f "data/weather.db" ]; then
  echo "weather.db exists"
else
  echo "weather.db does not exist"
  exit 1  # Exit with non-zero code to indicate test failure
fi
