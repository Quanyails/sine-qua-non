from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass
class WordlistMeta:
    name: str
    path: str
    range: Tuple[int, int]
    source: str
    updated: str
    delimiter: str = ";"
    scale: float = field(init=False)

    DEFAULT_SCALE = [0, 50]

    def __post_init__(self):
        inmin, inmax = self.range
        inputspan = inmax - inmin

        outmin, outmax = self.DEFAULT_SCALE
        outputspan = outmax - outmin

        self.scale = outputspan / inputspan

    def extract(self) -> Dict[str, int]:
        result = {}

        with open(self.path, "r") as f:
            for line in f:
                word, score = line.strip().split(self.delimiter)
                key = word.upper().replace(" ", "") # normalize
                value = int(score) * self.scale
                result[key] = int(value)
        return result
