import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score


DATA_PATH = "data/UCI_Credit_Card.csv"
TARGET = "default.payment.next.month"


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


def train_and_save_models():
    df = load_data()

    X = df.drop(columns=[TARGET, "ID"])
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    os.makedirs("models", exist_ok=True)

    models = {
        "model_v1": Pipeline(steps=[
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
        ]),

        "model_v2": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            class_weight="balanced"
        )
    }

    for model_name, model in models.items():
        print("=" * 60)
        print(f"Training model: {model_name}")

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("F1-score:", f1_score(y_test, y_pred))
        print("\nClassification report:")
        print(classification_report(y_test, y_pred))
        print("\nConfusion matrix:")
        print(confusion_matrix(y_test, y_pred))

        model_path = f"models/{model_name}.joblib"
        joblib.dump(model, model_path)

        print(f"Model saved to: {model_path}")


if __name__ == "__main__":
    train_and_save_models()