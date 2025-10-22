# utils/csv_reader.py
import os
import csv

def read_login_data(file_path):
    """Read test data from CSV and return list of dicts"""
    full_path = os.path.abspath(file_path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Test data file not found: {full_path}")

    data = []
    with open(full_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data