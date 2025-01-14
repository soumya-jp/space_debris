import requests

url = "http://127.0.0.1:8000/predict/"

data = {
    "ECCENTRICITY": 0.01,
    "LAUNCH_DATE": 2022.0,
    "RCS_SIZE_LARGE": 1,
    "RCS_SIZE_SMALL": 0,
    "APOAPSIS": 7000.5,
    "SEMIMAJOR_AXIS": 10000.3,
    "MEAN_MOTION": 15.3,
    "INCLINATION": 98.1,
    "PERIOD": 96.5,
    "REV_AT_EPOCH": 2458000.0,
    "PERIAPSIS": 6500.7,
    "BSTAR": 0.003,
    "RCS_SIZE_MEDIUM": 0,
    "MEAN_MOTION_DOT": 0.05,
    "ARG_OF_PERICENTER": 100.0,
    "RA_OF_ASC_NODE": 180.0,
    "MEAN_ANOMALY": 45.0,
    "RCS_SIZE_UNKNOWN": 0,
    "MEAN_MOTION_DDOT": 0.02
}

response = requests.post(url, json=data)

if response.status_code == 200:
    prediction = response.json()
    print("Prediction:", prediction)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
