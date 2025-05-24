#!/bin/bash

URL="https://google.com"     # Pas dit aan naar jouw test-endpoint
OUTPUT_FILE="curl_timings.csv"
FORMAT_FILE="curl-format.txt"
ITERATIONS=100

# Maak format file aan met timing variabelen
cat > $FORMAT_FILE <<EOL
time_namelookup: %{time_namelookup}
time_connect: %{time_connect}
time_appconnect: %{time_appconnect}
time_pretransfer: %{time_pretransfer}
time_starttransfer: %{time_starttransfer}
time_total: %{time_total}
EOL

# Maak output CSV bestand met header
echo "iter,time_namelookup,time_connect,time_appconnect,time_pretransfer,time_starttransfer,time_total" > $OUTPUT_FILE

# Loop voor aantal iteraties
for i in $(seq 1 $ITERATIONS); do
    # Curl met timing info
    OUTPUT=$(curl -w "@$FORMAT_FILE" -o /dev/null -s $URL)

    # Parse output naar CSV-formaat
    NL=$(echo "$OUTPUT" | grep 'time_namelookup' | awk '{print $2}')
    CONN=$(echo "$OUTPUT" | grep 'time_connect' | awk '{print $2}')
    APP=$(echo "$OUTPUT" | grep 'time_appconnect' | awk '{print $2}')
    PRE=$(echo "$OUTPUT" | grep 'time_pretransfer' | awk '{print $2}')
    START=$(echo "$OUTPUT" | grep 'time_starttransfer' | awk '{print $2}')
    TOTAL=$(echo "$OUTPUT" | grep 'time_total' | awk '{print $2}')

    # Schrijf naar CSV
    echo "$i,$NL,$CONN,$APP,$PRE,$START,$TOTAL" >> $OUTPUT_FILE

    # Optioneel: progressie tonen
    echo "Iteratie $i voltooid"
done

echo "Test afgerond. Resultaten opgeslagen in $OUTPUT_FILE"
