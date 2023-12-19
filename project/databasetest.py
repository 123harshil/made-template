
import os

def test_db_files_created():

    db_file_1 = r"\data\Traffic.db"
    db_file_2 = r"\data\weather.db"

    if not os.path.exists(db_file_1):
        print(f"Error: {db_file_1} does not exist.")
    if not os.path.exists(db_file_2):
        print(f"Error: {db_file_2} does not exist.")

if __name__ == '__main__':
    test_db_files_created()