"""Available stats classes
"""
from abc import ABC, abstractmethod


class BaseOnlineStats(ABC):
    @abstractmethod
    def fit(X):
        pass


class OnlineMean(BaseOnlineStats):
    def __init__(self):
        self._sum = 0.0
        self._n = 0

    @property
    def n(self):
        return self._n

    @property
    def sum(self):
        return self._sum

    def fit(self, X):
        self._n += 1
        self._sum += X

    def get(self):
        return self._sum / self._n


class OnlineVar(BaseOnlineStats):
    def __init__(self):
        self.online_mean = OnlineMean()
        self._sum_squared_diff = 0.0

    def fit(self, X):
        self.online_mean.fit(X)
        current_mean = self.online_mean.get()
        squared_diff = (X - current_mean) ** 2
        self._sum_squared_diff += squared_diff

    def get(self):
        n = self.online_mean.n
        return float(1.0 / (n - 1)) * self._sum_squared_diff
