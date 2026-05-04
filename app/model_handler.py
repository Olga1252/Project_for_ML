import joblib
import pandas as pd


MODEL_PATHS = {
    "v1": "models/model_v1.joblib",
    "v2": "models/model_v2.joblib"
}


FEATURE_COLUMNS = [
    "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE",
    "PAY_0", "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6",
    "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6",
    "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
]


def load_model(version="v1"):
    if version not in MODEL_PATHS:
        version = "v1"

    model_path = MODEL_PATHS[version]
    model = joblib.load(model_path)
    return model


def make_prediction(input_data, version="v1"):
    model = load_model(version)

    df = pd.DataFrame([input_data])
    df = df[FEATURE_COLUMNS]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "model_version": version,
        "prediction": int(prediction),
        "default_probability": float(probability)
    }