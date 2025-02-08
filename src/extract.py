from abc import ABC, abstractmethod
from model import XYPair

class PairBuilder(ABC):
    @abstractmethod
    def from_row(self, row: list[str]) -> XYPair:
        pass

class Series1Pair(PairBuilder):
    def from_row(self, row: list[str]) -> XYPair:
        return XYPair(x=row[0], y=row[1])

class Series2Pair(PairBuilder):
    def from_row(self, row: list[str]) -> XYPair:
        return XYPair(x=row[0], y=row[2])

class Series3Pair(PairBuilder):
    def from_row(self, row: list[str]) -> XYPair:
        return XYPair(x=row[0], y=row[3])

class Series4Pair(PairBuilder):
    def from_row(self, row: list[str]) -> XYPair:
        return XYPair(x=row[4], y=row[5])