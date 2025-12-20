import pandas as pd

def engineer_features(df):
    # convert time column to datetime
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # extract hour from timestamp
    df["hour"] = df["time"].dt.hour

    return df