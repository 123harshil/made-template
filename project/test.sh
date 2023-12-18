import unittest
import os

class TestDataPipeline(unittest.TestCase):
    def test_db_files_created(self):
        # Run your data pipeline here (replace this with the code to execute your pipeline)
        # Ensure the pipeline generates .db files in the /data directory
        
        # Check if .db files exist
        db_file_1 = "D:\project2\Traffic.db"
        db_file_2 = "D:\project2\weather.db"
        
        self.assertTrue(os.path.exists(db_file_1), f"{db_file_1} does not exist.")
        self.assertTrue(os.path.exists(db_file_2), f"{db_file_2} does not exist.")

if __name__ == '__main__':
    unittest.main()


