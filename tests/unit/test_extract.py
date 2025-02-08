import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from unittest.mock import Mock, sentinel, call
from extract import Series1Pair, Series2Pair, Series3Pair, Series4Pair

def test_series1pair():
    mock_raw_class = Mock()
    p1 = Series1Pair()
    xypair = p1.from_row([sentinel.X, sentinel.Y])
    assert xypair.x == sentinel.X
    assert xypair.y == sentinel.Y

# Similarly, implement tests for Series2Pair, Series3Pair, Series4Pair