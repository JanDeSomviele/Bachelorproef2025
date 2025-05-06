#!/bin/bash

# TARGET_IP="192.168.1.50"    # <-- Vul hier het IP-adres in van je controller
TARGET_IP="192.168.1.7"
OUTPUT="wifi_ping_results.csv"
i=1
echo "Tijd(ms);TTL;Verlies" > $OUTPUT

while [ $i -lt 51 ]
do
  PING=$(ping $TARGET_IP | grep 'TTL=')
  if [ -n "$PING" ]; then
    TIME=$(echo $PING | sed -n 's/.*time=\([0-9.]*\).*/\1/p')
    TTL=$(echo $PING | sed -n 's/.*TTL=\([0-9]*\).*/\1/p')
    echo "$TIME;$TTL;0" >> $OUTPUT
    i=$(( i + 1 ))
  else
    echo "0;0;1" >> $OUTPUT
    i=$(( i + 1 ))
  fi
  sleep 1
done

echo "✅ Ping test afgerond. Resultaten in $OUTPUT."
