"""Test suite for stats
"""
import pytest
import numpy as np

from online_stats.stats import OnlineMean, OnlineVar
from online_stats.streamer import file_reader


@pytest.fixture
def random_num_gen():
    rng = np.random.default_rng()
    random_gen = rng.integers(3, size=5000)
    return random_gen


def test_OnlineMean(random_num_gen):
    o_m = OnlineMean()

    for number in random_num_gen:
        o_m.fit(number)

    np.testing.assert_approx_equal(o_m.get(), 1, significant=2)


def test_OnlineVar(random_num_gen):
    o_var = OnlineVar()

    for number in random_num_gen:
        o_var.fit(number)

    expected_var = float((2 - 0 + 1) ** 2 - 1) / 12

    np.testing.assert_approx_equal(o_var.get(), expected_var, significant=2)
