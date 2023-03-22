import requests
import json
import csv

# Load the JSON data from a file
response = requests.get('https://cxserver.wikimedia.org/v2/list/mt')
data = json.loads(response.text)

# Open a new CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['source language', 'target language', 'engine name'])

    # Loop through the JSON data and write each row to the CSV file
    for engine_name, languages in data.items():
        for source_language, target_languages in languages.items():
            for target_language in target_languages:
                if engine_name == 'defaults':
                    continue
                writer.writerow([source_language, target_language, engine_name])

import requests
import json
import csv

# Load the JSON data from a file
response = requests.get('https://cxserver.wikimedia.org/v2/list/mt')
data = json.loads(response.text)

# Open a new CSV file for writing
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(['source language', 'target language', 'engine name'])

    # Loop through the JSON data and write each row to the CSV file
    for engine_name, languages in data.items():
        for source_language, target_languages in languages.items():
            for target_language in target_languages:
                if engine_name == 'defaults':
                    continue
                writer.writerow([source_language, target_language, engine_name])

