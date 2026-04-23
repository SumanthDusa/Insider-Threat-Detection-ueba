import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "dataset", "ueba_dataset.csv")
MODEL_FILE = os.path.join(BASE_DIR, "ueba_model.pkl")

df = pd.read_csv(DATA_FILE)

X = df[["file_count", "usb_flag", "login_hour"]]

model = IsolationForest(contamination=0.2)
model.fit(X)

with open(MODEL_FILE, "wb") as f:
    pickle.dump(model, f)

print("✅ UEBA model trained")