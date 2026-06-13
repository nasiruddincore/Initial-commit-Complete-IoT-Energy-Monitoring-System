import time
import random
import csv
import os

if not os.path.exists('data'):
    os.makedirs('data')

print("Simulation started. Press Ctrl+C to stop.")
while True:
    current = random.uniform(0.1, 5.0)
    power = 230.0 * current
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    with open('data/energy_logs.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, current, power])
        
    print(f'Logged: {power:.2f}W')
    time.sleep(2)
