KAGGLE_JSON_PATH="./project/kaggle.json"
KAGGLE_CONFIG_DIR=$(dirname "$KAGGLE_JSON_PATH")
export KAGGLE_CONFIG_DIR

python3 ./project/trafficprediction.py.py
