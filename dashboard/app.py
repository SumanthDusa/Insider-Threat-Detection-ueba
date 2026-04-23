from flask import Flask, render_template, request, redirect, session
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "secret123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "dataset", "live_events.csv")

USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['user'] = USERNAME
            return redirect('/dashboard')
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    df = pd.read_csv(DATA_FILE, on_bad_lines='skip')

    # 🕒 format time
    df["time"] = pd.to_datetime(df["time"], unit='s')
    df["time"] = df["time"].dt.strftime("%H:%M:%S")

    # ✅ FILTER ONLY SUSPICIOUS EVENTS
    suspicious_df = df[df["suspicious"] == 1]

    # fallback (important for demo)
    if suspicious_df.empty:
        suspicious_df = df.tail(20)

    table = suspicious_df.tail(20).to_html(
        classes='table table-dark table-hover align-middle',
        index=False,
        border=0
    )

    user_risk = df.groupby("user")["risk_score"].sum().reset_index()

    return render_template(
        "dashboard.html",
        table=table,
        users=user_risk.to_dict(orient="records"),
        times=df.tail(50).to_dict(orient="records")
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

app.run(port=5001, debug=True)