from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = FastAPI()

# Load model with error handling
try:
    model = joblib.load("opt_randomforest_model.pkl")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# Input data structure
class SpaceDebrisInput(BaseModel):
    ECCENTRICITY: float
    LAUNCH_DATE: float
    RCS_SIZE_LARGE: int
    RCS_SIZE_SMALL: int
    APOAPSIS: float
    SEMIMAJOR_AXIS: float
    MEAN_MOTION: float
    INCLINATION: float
    PERIOD: float
    REV_AT_EPOCH: float
    PERIAPSIS: float
    BSTAR: float
    RCS_SIZE_MEDIUM: int
    MEAN_MOTION_DOT: float
    ARG_OF_PERICENTER: float
    RA_OF_ASC_NODE: float
    MEAN_ANOMALY: float
    RCS_SIZE_UNKNOWN: int
    MEAN_MOTION_DDOT: float

# Convert input into a Pandas DataFrame
def preprocess_input(input_data: SpaceDebrisInput):
    data_dict = input_data.model_dump()

    # Convert dictionary to DataFrame with a single row
    df = pd.DataFrame([data_dict])

    return df

@app.post("/predict/")
def predict(input_data: SpaceDebrisInput):
    try:
        preprocessed_data = preprocess_input(input_data)
        prediction = model.predict(preprocessed_data)

        class_mapping = {
            0: "Debris",
            1: "Payload",
            2: "Rocket Body",
        }
        predicted_class = class_mapping.get(int(prediction[0]), "Unknown")

        return {"prediction": predicted_class}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Space debris classification model is running!"}
