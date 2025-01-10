#!/usr/bin/env python3
import sys
import csv

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()
    
    # Split the CSV line
    try:
        fields = next(csv.reader([line]))  # Use csv.reader to parse the line correctly
    except csv.Error:
        continue  # Skip any lines that can't be parsed correctly
    
    if fields[0] == "show_id":  # Skip header row
        continue
    
    # Extract country and genres (columns 5 and 10 respectively)
    country = fields[5]
    genres = fields[10].split(", ")
    
    # Emit each genre with a count of 1 if the country is Italy
    if "Italy" in country:
        for genre in genres:
            print(f"{genre}\t1\tItaly")  # Tag with "Italy" for filtering in reducer
    else:
        for genre in genres:
            print(f"{genre}\t1\tGlobal")  # Tag with "Global" for overall stats

