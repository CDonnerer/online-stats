"""Available stats classes
"""
from abc import ABC


class BaseOnlineStats(ABC):
    def fit(X):
        pass


class OnlineMean(BaseOnlineStats):
    def __init__(self):
        self._sum = 0.0
        self._n = 0

    def fit(self, X):
        self._n += 1
        self._sum += X

    def get(self):
        return self._sum / self._n
