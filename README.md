# Space Debris Classification Project

## Overview
This project focuses on classifying space debris objects using data preprocessing, visualization, and Machine Learning techniques. The dataset includes various features such as object size, orbital parameters, and launch information. The goal is to accurately predict the `OBJECT_TYPE` category. Future plans include integration of **Robot Operating System (ROS)** to simulate autonomous data collection and real-time classification within a robotic environment.

## Dataset
The dataset contains the following key features:
- **CREATION_DATE**: Date when the record was created.
- **OBJECT_NAME**: Name of the object.
- **OBJECT_ID**: Unique identifier for the object.
- **ORBITAL PARAMETERS**: Includes `MEAN_MOTION`, `ECCENTRICITY`, `INCLINATION`, etc.
- **RCS_SIZE**: Radar Cross Section, categorized as `SMALL`, `MEDIUM`, `LARGE`, or `UNKNOWN`.
- **COUNTRY_CODE**: Country responsible for the object.
- **LAUNCH_DATE**: Date the object was launched.
- **OBJECT_TYPE**: Target variable (e.g., DEBRIS, PAYLOAD, ROCKET BODY).

## Project Workflow and Current Progress
### Data Preprocessing
- Removed irrelevant or redundant columns.
- Handled missing values:
  - Replaced missing values in `RCS_SIZE` with `UNKNOWN`.
  - Used mode for categorical fields such as `COUNTRY_CODE` and `LAUNCH_DATE`.
- Encoded categorical variables:
  - One-hot encoded `RCS_SIZE`.
  - Label-encoded `OBJECT_TYPE`.
- Verified no null values remain in the dataset.

### Notes
- Columns such as `OBJECT_NAME` and `OBJECT_ID` may not be used for modeling due to low relevance.
- Target variable (`OBJECT_TYPE`) has been label-encoded for machine learning.

## Next Steps
### Preprocessing of Features:
1. Scale numeric features as needed.
2. Perform feature engineering and data visualization.
3. Train-test split to prepare data for machine learning models.

### ML Modeling:
1. Model Selection
2. Model Training and Evaluation
3. Model Tuning
4. Model Deployment

### ROS Integration Plans:
1. Set up ROS environment with simulated debris objects.
2. Develop ROS nodes for real-time data collection and classification.
3. Integrate ML models with ROS for autonomous decision-making.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.

## Contributors
- Soumya Bhavaraju

## Acknowledgments
This project leverages open data sources (Kaggle) for space debris and orbital objects.
