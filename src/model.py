from dataclasses import dataclass, asdict

@dataclass
class XYPair:
    x: str
    y: str

    def asdict(self):
        return asdict(self)