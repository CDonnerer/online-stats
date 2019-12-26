"""Test suite for data streamer
"""

from online_stats.streamer import file_reader


def test_file_reader():
    # from IPython import embed
    #
    # embed()

    file_gen = file_reader("tests/data/numbers.dat")
