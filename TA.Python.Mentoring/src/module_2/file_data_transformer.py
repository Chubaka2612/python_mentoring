import csv
import json


def read_csv_file(filename):
    results = {"cars": []}
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            results["cars"].append(row)
    return results


def write_to_json_file(filename, data):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=2)
