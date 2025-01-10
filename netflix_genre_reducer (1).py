#!/usr/bin/env python3
import sys

current_genre = None
italy_count = 0
global_count = 0

# Read each key-value pair from standard input
for line in sys.stdin:
    line = line.strip()
    genre, count, tag = line.split("\t")
    
    # Convert count from string to int
    try:
        count = int(count)
    except ValueError:
        continue

    # New genre encountered
    if genre != current_genre and current_genre is not None:
        # Output results for the previous genre
        print(f"{current_genre}\tItaly\t{italy_count}")
        print(f"{current_genre}\tGlobal\t{global_count}")
        
        # Reset counts for the new genre
        italy_count = 0
        global_count = 0

    current_genre = genre
    
    # Accumulate counts based on tag
    if tag == "Italy":
        italy_count += count
    elif tag == "Global":
        global_count += count

# Output the last genre
if current_genre:
    print(f"{current_genre}\tItaly\t{italy_count}")
    print(f"{current_genre}\tGlobal\t{global_count}")

