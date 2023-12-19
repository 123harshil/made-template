import os

def check_database_files():
    data_directory = 'data'  # Replace with the path to your data directory
    
    # Check if traffic.db exists
    traffic_db_path = os.path.join(data_directory, 'traffic.db')
    if os.path.exists(traffic_db_path):
        print("traffic.db exists")
    else:
        print("traffic.db does not exist")

    # Check if weather.db exists
    weather_db_path = os.path.join(data_directory, 'weather.db')
    if os.path.exists(weather_db_path):
        print("weather.db exists")
    else:
        print("weather.db does not exist")

# Execute the function to check the database files
check_database_files()
