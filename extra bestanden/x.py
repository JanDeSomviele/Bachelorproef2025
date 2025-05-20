import requests
import time

BRIDGE_IP = "192.168.1.22"
USERNAME = "DUgpSWs4X6tY9ytE-sDjKmePO7JcDrN9rKWdKr-G"
LIGHT_ID = "1"
URL = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/{LIGHT_ID}/state"

def toggle_light(state):
    payload = { "on": state }
    start = time.time()
    r = requests.put(URL, json=payload)
    end = time.time()
    if r.status_code == 200:
        print(f"{'Aan' if state else 'Uit'} - Reactietijd: {round((end - start)*1000, 2)} ms")
    else:
        print("Fout:", r.text)

# 20 keer aan en uit schakelen
for i in range(20):
    toggle_light(True)
    time.sleep(1)
    toggle_light(False)
    time.sleep(1)
