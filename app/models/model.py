import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

model = None  # Global model
dataset_path = "data/dataset_500_balanced.csv"  # Default dataset path


def train_model():
    global model
    # Load dataset
    data = pd.read_csv(dataset_path)
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Save the trained model
    joblib.dump(model, "model.pkl")

    return {"accuracy": accuracy, "f1_score": f1}


def make_prediction(data):
    global model
    if model is None:
        # Load the model if it's not already loaded
        try:
            model = joblib.load("model.pkl")
        except FileNotFoundError:
            return {"error": "Model not trained yet"}

    # Make prediction
    features = [[data["Temperature"], data["Run_Time"]]]
    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])

    return {"Downtime": "Yes" if prediction else "No", "Confidence": confidence}
