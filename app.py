from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = FastAPI()

model = joblib.load("opt_randomforest_model.pkl")

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

# Define a function to preprocess input data (no scaling involved)
def preprocess_input(input_data: SpaceDebrisInput):
    # Convert input data into a list
    data_dict = input_data.dict()

    # List the features in the correct order, according to your model's training setup
    feature_values = [
        data_dict['ECCENTRICITY'],
        data_dict['LAUNCH_DATE'],  # You may need to convert this to a numeric value (e.g., timestamp)
        data_dict['RCS_SIZE_LARGE'],
        data_dict['RCS_SIZE_SMALL'],
        data_dict['APOAPSIS'],
        data_dict['SEMIMAJOR_AXIS'],
        data_dict['MEAN_MOTION'],
        data_dict['INCLINATION'],
        data_dict['PERIOD'],
        data_dict['REV_AT_EPOCH'],
        data_dict['PERIAPSIS'],
        data_dict['BSTAR'],
        data_dict['RCS_SIZE_MEDIUM'],
        data_dict['MEAN_MOTION_DOT'],
        data_dict['ARG_OF_PERICENTER'],
        data_dict['RA_OF_ASC_NODE'],
        data_dict['MEAN_ANOMALY'],
        data_dict['RCS_SIZE_UNKNOWN'],
        data_dict['MEAN_MOTION_DDOT']
    ]

    return np.array([feature_values])

@app.post("/predict/")
def predict(input_data: SpaceDebrisInput):
    preprocessed_data = preprocess_input(input_data)

    prediction = model.predict(preprocessed_data)


    class_mapping = {
        0: "Debris",
        1: "Payload",
        2: "Rocket Body",
    }

    predicted_class = class_mapping.get(int(prediction[0]), "Unknown")

    return {"prediction": predicted_class}
@app.get("/")
def read_root():
    return {"message": "Space debris classification model is running!"}
