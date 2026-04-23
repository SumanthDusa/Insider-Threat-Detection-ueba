from flask import Flask, request, jsonify
from detection_engine import process_event

app = Flask(__name__)

@app.route('/event', methods=['POST'])
def receive_event():
    event = request.json
    print("📥 Received:", event)   # ADD THIS
    result = process_event(event)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)