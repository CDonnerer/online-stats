"""Ties together stats and streamer
"""
from online_stats.stats import OnlineMean
from online_stats.streamer import file_reader


def get_info(path_to_data):
    """
    """
    om = OnlineMean()
    file_gen = file_reader(path_to_data)

    for row in file_gen:
        om.fit(float(row[0]))

    return om.get()
