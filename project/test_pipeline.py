import unittest
import os
from unittest.mock import patch
from pipeline import (
    download_traffic_data, create_traffic_table, insert_traffic_data,
    create_weather_table, insert_weather_data
)

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = os.path.abspath('test_data')
        os.makedirs(self.test_data_dir, exist_ok=True)

    def tearDown(self):
        os.rmdir(self.test_data_dir)

    @patch('pipeline.download_traffic_data')
    @patch('pipeline.create_traffic_table')
    @patch('pipeline.insert_traffic_data')
    @patch('pipeline.create_weather_table')
    @patch('pipeline.insert_weather_data')
    def test_data_pipeline(self, mock_insert_weather_data, mock_create_weather_table, mock_insert_traffic_data, mock_create_traffic_table, mock_download_traffic_data):
        mock_download_traffic_data.return_value = None
        mock_create_traffic_table.return_value = (None, None)
        mock_insert_traffic_data.return_value = None
        mock_create_weather_table.return_value = (None, None)
        mock_insert_weather_data.return_value = None

        print("Running the data pipeline...")
        download_traffic_data()

        traffic_con, traffic_cursor = create_traffic_table()
        insert_traffic_data(traffic_con, traffic_cursor)

        weather_con, weather_cursor = create_weather_table()
        insert_weather_data(weather_con, weather_cursor)

        print("Data pipeline execution complete.")

        # Check if the output files exist
        self.assertTrue(os.path.exists('Traffic.db'))
        self.assertTrue(os.path.exists('weather.db'))

if __name__ == '__main__':
    unittest.main()
