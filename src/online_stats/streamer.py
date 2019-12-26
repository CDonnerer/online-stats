"""Module for streaming data from file
"""


def file_reader(path):
    with open(path) as file:
        for row in file:
            yield row.split(",")[:-1]
