import requests
import time
import csv
from datetime import datetime

BRIDGE_IP = "192.168.1.22"
USERNAME = "DUgpSWs4X6tY9ytE-sDjKmePO7JcDrN9rKWdKr-G"
LIGHT_ID = "1"
URL = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/{LIGHT_ID}/state"
AANTAL_TESTS = 200
CSV_BESTAND = f"betrouwbaarheid_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

def toggle_light(state):
    payload = {"on": state}
    start = time.time()
    try:
        response = requests.put(URL, json=payload, timeout=5)
        end = time.time()
        duur = round((end - start)*1000, 2)  # in ms

        if response.status_code == 200:
            return True, duur, response.json()
        else:
            return False, duur, response.text
    except Exception as e:
        return False, None, str(e)

# === TESTLOOP ===
resultaten = []
print(f"Start betrouwbaarheidstest ({AANTAL_TESTS} commando’s)...")

for i in range(AANTAL_TESTS):
    state = i % 2 == 0  # om en om: aan/uit
    success, duur, reactie = toggle_light(state)

    resultaten.append({
        "nummer": i + 1,
        "actie": "aan" if state else "uit",
        "resultaat": "succes" if success else "fout",
        "reactietijd_ms": duur if duur else "n.v.t.",
        "response": reactie
    })

    status = "true" if success else "false"
    print(f"[{i+1:03}] {status} - {'aan' if state else 'uit'} - {duur if duur else 'n.v.t.'} ms")

    time.sleep(1)  # optioneel vertraging tussen commando’s

# === RESULTATEN SCHRIJVEN NAAR CSV ===
with open(CSV_BESTAND, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=resultaten[0].keys())
    writer.writeheader()
    writer.writerows(resultaten)

# === OVERZICHT TONEN ===
aantal_succes = sum(1 for r in resultaten if r["resultaat"] == "succes")
aantal_fout = AANTAL_TESTS - aantal_succes
gemiddelde_tijd = round(sum(r["reactietijd_ms"] for r in resultaten if isinstance(r["reactietijd_ms"], float)) / aantal_succes, 2)

print("\nRESULTAATOVERZICHT")
print(f"Succesvolle commando's : {aantal_succes}")
print(f"Mislukte commando's     : {aantal_fout}")
print(f"Gemiddelde reactietijd : {gemiddelde_tijd} ms")
print(f"CSV opgeslagen als: {CSV_BESTAND}")