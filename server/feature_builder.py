def build_features(event):
    return [
        event.get("file_count", 1),
        1 if event['type'] == 'usb' else 0,
        int(event.get("time", 0) % 86400 / 3600)
    ]