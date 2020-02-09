"""Module for streaming data from file
"""
import csv


def file_reader(path):
    with open("random.csv") as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            yield row.split(",")[:-1]
