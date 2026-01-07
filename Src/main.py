from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import pandas as pd
import shutil
from Src.predict import evaluate_model
from Src.ingest import load_weather_data
from Src.process import prepare_weather_features
from Src.predict import train_statistical_model, predict_from_user_input

app = FastAPI(
    title="A Cloud-Based Weather Prediction System"
)

DATA_PATH = "data/weather_classification_data.csv"


#  Root URL → Redirect to Swagger UI
@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.post("/load-data")
async def upload_dataset(file: UploadFile = File(...)):
    with open(DATA_PATH, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"status": "Dataset uploaded successfully"}


# -------- USER INPUT SCHEMA --------
class WeatherInput(BaseModel):
    Temperature: float
    Humidity: float
    Wind_Speed: float
    Pressure: float


@app.post("/predict")
def predict_weather(input_data: WeatherInput):
    # 1. Load dataset for training
    dataset_df = load_weather_data(DATA_PATH)

    # 2. Prepare features
    train_df = prepare_weather_features(dataset_df)

    # 3. Train model
    model = train_statistical_model(train_df)

    # 4. Convert user input to DataFrame
    user_df = pd.DataFrame([{
        "Temperature": input_data.Temperature,
        "Humidity": input_data.Humidity,
        "Wind_Speed": input_data.Wind_Speed,
        "Pressure": input_data.Pressure,
    }])

    # 5. Predict result
    result_df = predict_from_user_input(model, user_df)

    return result_df.to_dict(orient="records")[0]


@app.get("/metrics")
def model_metrics():
    dataset_df = load_weather_data(DATA_PATH)
    train_df = prepare_weather_features(dataset_df)

    model = train_statistical_model(train_df)
    metrics = evaluate_model(model, train_df)

    return {
        "model": "Statistical Classification Model",
        "evaluation": metrics
    }
