import time, random, requests

SERVER_URL = "http://127.0.0.1:5000/event"
users = ["alice", "bob", "charlie"]

def send(e):
    requests.post(SERVER_URL, json=e)
    print("Simulated:", e)

while True:
    if random.random() < 0.8:
        e = {
            "type": random.choice(["login", "file_access"]),
            "user": random.choice(users),
            "file_count": random.randint(1, 5),
            "time": time.time()
        }
    else:
        e = {
            "type": random.choice(["usb", "file_access"]),
            "user": random.choice(users),
            "file_count": random.randint(25, 100),
            "time": time.time()
        }

    send(e)
    time.sleep(2)