import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def train_statistical_model(df: pd.DataFrame):
    """
    Train lightweight statistical classification model.
    """

    X = df[["Temperature", "Humidity", "Wind_Speed", "Pressure"]]
    y = df["Target"]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    return model


def predict_from_user_input(model, user_df: pd.DataFrame):
    """
    Predict advisory and confidence score.
    """

    X = user_df[["Temperature", "Humidity", "Wind_Speed", "Pressure"]]

    prediction = model.predict(X)
    probabilities = model.predict_proba(X)
    confidence = probabilities.max(axis=1)

    label_map = {
        0: "Avoid going outside",
        1: "Go outside with caution",
        2: "Safe to go outside"
    }

    result_df = user_df.copy()
    result_df["Advisory"] = [label_map[p] for p in prediction]
    result_df["Confidence"] = confidence.round(2)

    return result_df


def evaluate_model(model, df: pd.DataFrame):
    """
    Evaluate model correctness using standard classification metrics.
    """

    X = df[["Temperature", "Humidity", "Wind_Speed", "Pressure"]]
    y_true = df["Target"]

    y_pred = model.predict(X)

    return {
        "accuracy": round(accuracy_score(y_true, y_pred), 2),
        "precision": round(
            precision_score(y_true, y_pred, average="weighted"), 2
        ),
        "recall": round(
            recall_score(y_true, y_pred, average="weighted"), 2
        ),
        "f1_score": round(
            f1_score(y_true, y_pred, average="weighted"), 2
        )
    }