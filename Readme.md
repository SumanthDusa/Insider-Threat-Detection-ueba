 Insider Threat Detection System (UEBA)

 Overview

This project implements an Insider Threat Detection System using User and Entity Behavior Analytics (UEBA).
It analyzes user activities such as logins, file access, and USB usage to detect anomalous behavior that may indicate security threats.

Unlike traditional security systems, this solution focuses on internal users who already have authorized access.

---

 Features

-  Detects abnormal user behavior in real-time
-  Uses machine learning (Isolation Forest) for anomaly detection
-  Monitors activities like:
  - Login time
  - File access frequency
  - USB usage
-  Lightweight and efficient system
-  Flask-based dashboard for visualization

---

 Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Psutil

---

📂 Project Structure

insider threat detection system UEBA/
├── Dataset/
│   ├── live_events.csv      # Test/Live data
│   └── ueba_dataset.csv     # Training Dataset
├── Server/
│   ├── api.py               #API Server
│   ├── detection_engine.py  # Core Detection Logic
│   ├── feature_builder.py   # Feature Extraction
│   ├── rules_engine.py      # Rule-based checks
│   └── train_ueba_model.py  # Training Script
├── Client/
│   ├── monitor.py           # Sends live data
│   └── simulator.py         # Generates user Activity
├── Dashboard/
│   ├── app.py               # Flask Dashboard
│   └── templates/
│       ├── dashboard.html
│       ├── index.html
│       └── login.html
└── Models/
    └── ueba_model.pkl       # Trained ML Model

---

 Dataset Description

The system uses a structured dataset with the following fields:

Column| Description
type| Activity type (login / file_access)
time| Timestamp of activity
file_count| Number of files accessed
usb_flag| USB usage (1 = Yes, 0 = No)
login_hour| Hour of login (0–23)

---

 Machine Learning Approach

This project uses Isolation Forest Algorithm:

- Works on unsupervised learning
- Identifies rare or unusual patterns
- Efficient for anomaly detection in large datasets

---

 How to Run the Project

1.Install dependencies

pip install -r requirements.txt

2️. Run the application

python app.py

3️. Open in browser

http://127.0.0.1:5000/

---

 How It Works

1. User activity data is collected (simulator/monitor)
2. Features are extracted using "feature_builder.py"
3. Data is analyzed using the trained ML model
4. Suspicious activities are flagged
5. Results are displayed on the dashboard

---

 Example Suspicious Behavior

- High file access count at unusual hours
- Login during late night (0–3 AM)
- USB usage combined with large data access

---

 Use Case

This system helps organizations:

- Detect insider threats
- Prevent data leakage
- Improve internal security monitoring


 Future Improvements

- Real-time alert system (email/SMS)
- Integration with enterprise security tools
- Advanced deep learning models
- Role-based behavior analysis

