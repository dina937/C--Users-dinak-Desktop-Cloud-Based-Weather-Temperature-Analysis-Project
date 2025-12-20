import numpy as np

def station_mean_predict(df):
    try:
        return round(float(df["value"].mean()), 2)
    except:
        return "insufficient data"

def station_hour_predict(df):
    try:
        hour_groups = df.groupby("hour")["value"].mean()
        return hour_groups.to_dict()
    except:
        return "insufficient data"