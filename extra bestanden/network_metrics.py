# network_metrics.py
import argparse
import csv
import time
from ping3 import ping
import psutil
import speedtest

def collect_metrics(target, interval, duration):
    start_time = time.time()
    results = []

    while (time.time() - start_time) < duration:
        latency = ping(target, unit='ms')
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        results.append([timestamp, latency, cpu, mem])
        print(f"{timestamp} | Latency: {latency:.2f} ms | CPU: {cpu}% | RAM: {mem}%")
        time.sleep(interval)

    return results

def write_csv(results, filename="network_results.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Latency (ms)', 'CPU (%)', 'RAM (%)'])
