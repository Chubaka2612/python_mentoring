import csv
import json


def read_csv_file(filename):
    results = {"cars": []}
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        [results["cars"].append(row) for row in reader]
    return results


def write_to_json_file(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=2)
