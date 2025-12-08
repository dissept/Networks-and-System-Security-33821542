import random

def detect_anomalies():
    outbound_connections = random.randint(0, 200)

    if outbound_connections > 100:
        print(f"[ALERT] Excessive outbound traffic: {outbound_connections} connections")

    port_scans = random.choice([0, 0, 0, 1])  # 25% chance of scan
    if port_scans:
        print("[ALERT] Possible port scan detected")

    failed_logins = random.randint(0, 10)
    if failed_logins > 5:
        print(f"[ALERT] Abnormal failed login attempts: {failed_logins}")

print("Starting network monitor...\n")

for _ in range(10):
    detect_anomalies()
    time.sleep(1)
