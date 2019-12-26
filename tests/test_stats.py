"""Test suite for stats
"""
import numpy as np

from online_stats.stats import OnlineMean
from online_stats.streamer import file_reader


def test_OnlineMean():
    rng = np.random.default_rng()
    random_gen = rng.integers(3, size=100)

    om = OnlineMean()

    for number in random_gen:
        om.fit(number)
        print(om.get())
