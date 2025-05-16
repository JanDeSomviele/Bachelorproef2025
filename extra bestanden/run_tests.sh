#!/bin/bash
mkdir -p logs
DATE=$(date +"%Y%m%d_%H%M%S")

echo "Start netwerkmeting..."
python3 network_metrics.py --target 8.8.8.8 --interval 5 --duration 60 > logs/network_$DATE.csv

echo "Start Modbus polling..."
python3 modbus_poll.py --host 127.0.0.1 --port 5020 --unit 1 --count 10 > logs/modbus_$DATE.txt

echo "Tests afgerond. Logs opgeslagen in ./logs/"
