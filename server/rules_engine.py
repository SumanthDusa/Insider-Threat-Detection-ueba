def rule_score(event):
    risk = 0

    if event['type'] == 'usb':
        risk += 40

    if event['type'] == 'file_access' and event.get("file_count", 1) > 20:
        risk += 35

    hour = int(event.get("time", 0) % 86400 / 3600)
    if event['type'] == 'login' and (hour < 6 or hour > 22):
        risk += 25

    return risk