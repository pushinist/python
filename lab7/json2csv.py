import json
import csv


file_name = input()
with open(f"./lab7/{file_name}", 'r') as f:
    json_data = json.load(f)


data = json_data[(list(dict.items(json_data))[0])[0]]

with open(f"./lab7/{file_name[:-4]}csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    count = 0
    for item in data:
        if count == 0:
            header = item.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(item.values())





