import pickle
import os
import pandas as pd
from feature_builder import build_features

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "ueba_model.pkl")
DATA_FILE = os.path.join(BASE_DIR, "..", "dataset", "live_events.csv")

with open(MODEL_FILE, "rb") as f:
    model = pickle.load(f)

def process_event(event):
    features = build_features(event)
    ml_score = model.decision_function([features])[0]

    attempts = int(event.get("file_count", 1))

    # 🔥 RULE BASED RISK
    if attempts > 70:
        rule_risk = 8
    elif attempts > 40:
        rule_risk = 6
    elif attempts > 20:
        rule_risk = 4
    else:
        rule_risk = 1

    # 🔥 ML contribution
    ml_risk = 3 if ml_score < -0.2 else 1

    # ✅ FINAL RISK (1–10)
    risk_score = min(10, rule_risk + ml_risk)

    save_event(event, attempts, risk_score)

    return {"risk_score": risk_score}


def save_event(event, attempts, risk_score):
    df = pd.DataFrame([{
        "user": event.get("user", "unknown"),
        "type": event["type"],
        "time": event["time"],
        "attempts": attempts,
        "risk_score": risk_score,
        "suspicious": 1 if risk_score >= 7 else 0
    }])

    if not os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, index=False)
    else:
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)