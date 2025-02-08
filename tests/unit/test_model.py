import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from model import XYPair
from unittest.mock import sentinel
from dataclasses import asdict

def test_xypair():
    pair = XYPair(x=sentinel.X, y=sentinel.Y)
    assert pair.x == sentinel.X
    assert pair.y == sentinel.Y
    assert asdict(pair) == {"x": sentinel.X, "y": sentinel.Y}