from dataclasses import dataclass


@dataclass
class Hub:
    name: str
    x: float
    y: float
    color: str


@dataclass
class Connection:
    source: str
    destination: str
