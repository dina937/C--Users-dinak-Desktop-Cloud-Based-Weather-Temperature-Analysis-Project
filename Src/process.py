def decide_target(row):
    """
    Weather risk classification based on Temperature (°C) and Humidity (%).
Target labels:
    0 = Avoid   (Extreme / risky weather)
    1 = Caution (Moderate risk)
    2 = Safe    (Normal conditions)
    """

    temp = row["Temperature"]
    humidity = row["Humidity"]

    # Extreme / invalid values
    if temp < -40 or temp > 55 or humidity < 0 or humidity > 100:
        return 2

    if temp >= 38 and humidity >= 75:
        return 0
    elif temp >= 32 or humidity >= 65:
        return 1
    elif temp < 0:
        return 1
    else:
        return 2


def prepare_weather_features(df):
    df = df.copy()
    df["Target"] = df.apply(decide_target, axis=1)
    return df