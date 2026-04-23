import time, os, requests, psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SERVER_URL = "http://127.0.0.1:5000/event"

def send_event(event):
    try:
        requests.post(SERVER_URL, json=event)
        print("📤 Sent:", event)
    except Exception as e:
        print("Error:", e)

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            send_event({
                "type": "file_access",
                "user": "real_user",
                "file_count": 1,
                "time": time.time()
            })

def detect():
    for u in psutil.users():
        send_event({
            "type": "login",
            "user": u.name,
            "file_count": 1,
            "time": time.time()
        })

observer = Observer()

# ✅ FIXED LINE
observer.schedule(Handler(), path=".", recursive=True)

observer.start()

print("🖥️ Monitoring started...")

try:
    while True:
        detect()
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()