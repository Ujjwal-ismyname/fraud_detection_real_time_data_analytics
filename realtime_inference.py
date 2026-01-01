# import pandas as pd
# import joblib
# import time
# from feature_engineering import create_features

# model = joblib.load("fraud_model.pkl")

# def run_inference():
#     while True:
#         try:
#             df = pd.read_csv("current_transaction.csv")
#             X, _ = create_features(df)
#             pred = model.predict(X)[0]
#             prob = model.predict_proba(X)[0][1]

#             df["fraud_prediction"] = pred
#             df["fraud_probability"] = round(prob, 3)
#             df.to_csv("prediction_output.csv", index=False)

#             print(f" Fraud: {pred} | Probability: {prob:.2f}")
#             time.sleep(1)

#         except Exception:
#             time.sleep(1)

# if __name__ == "__main__":
#     run_inference()

import pandas as pd
import joblib
import time
import os
from feature_engineering import create_features

MODEL_PATH = "fraud_model.pkl"
INPUT_FILE = "current_transaction.csv"
OUTPUT_FILE = "prediction_output.csv"

model = joblib.load(MODEL_PATH)

last_modified_time = None

def run_realtime_inference():
    global last_modified_time
    print("⚡ Real-time inference started")

    while True:
        try:
            # Check if new data arrived
            current_mtime = os.path.getmtime(INPUT_FILE)

            if last_modified_time is None or current_mtime != last_modified_time:
                last_modified_time = current_mtime

                df = pd.read_csv(INPUT_FILE)

                X, _ = create_features(df)

                preds = model.predict(X)
                probs = model.predict_proba(X)[:, 1]

                df["fraud_prediction"] = preds
                df["fraud_probability"] = probs.round(3)

                df.to_csv(OUTPUT_FILE, index=False)

                print(f" Inferred {len(df)} transaction(s)")

            # Tiny sleep to prevent CPU burn
            time.sleep(0.05)

        except FileNotFoundError:
            time.sleep(0.1)

if __name__ == "__main__":
    run_realtime_inference()