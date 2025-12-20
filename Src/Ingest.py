import pandas as pd

def load_data():
    try:
        df = pd.read_csv("app/Weather_classification_data.csv")
        return df
    except FileNotFoundError:
        raise Exception("Weather_classification_data.csv is missing from /app")