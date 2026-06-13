import time
import random
import csv
import os

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

file_path = os.path.join('data', 'energy_logs.csv')

print(f"Logging data to: {os.path.abspath(file_path)}")

while True:
    current = random.uniform(0.1, 5.0)
    power = 230.0 * current
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, current, power])
    
    print(f"[{timestamp}] Logged: {power:.2f}W")
    time.sleep(2)