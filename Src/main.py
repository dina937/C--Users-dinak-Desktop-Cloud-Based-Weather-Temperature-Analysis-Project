from fastapi import FastAPI
from ingest import load_data
from process import engineer_features
from predict import station_mean_predict, station_hour_predict

app = FastAPI()

@app.get("/analyze")
def analyze():
    df = load_data()
    df = engineer_features(df)
    mean_prediction = station_mean_predict(df)
    hour_prediction = station_hour_predict(df)
    return {
        "station_mean_prediction": mean_prediction,
        "station_hour_prediction": hour_prediction
    }

@app.get("/status")
def status():
    return {"status": "system running successfully"}