import pandas as pd
from pathlib import Path


def load_weather_data(csv_path: str) -> pd.DataFrame:
    """
    Load and normalize weather dataset.
    Target is NOT loaded from dataset.
    Target will be created in process.py.
    """

    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # Normalize column names
    df.columns = df.columns.str.lower().str.strip()

    # Rename dataset-specific columns
    column_mapping = {
        "temperature (c)": "Temperature",
        "humidity": "Humidity",
        "wind_speed(km/h)": "Wind_Speed",
        "pressure(millibars)": "Pressure"
    }

    df = df.rename(columns=column_mapping)

    required_columns = [
        "Temperature",
        "Humidity",
        "Wind_Speed",
        "Pressure"
    ]

    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        raise ValueError(
            f"Required columns missing after inspection: {missing}\n"
            f"Found columns: {list(df.columns)}"
        )

    df = df.dropna(subset=required_columns)

    return df