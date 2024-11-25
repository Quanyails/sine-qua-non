from dataclasses import dataclass
from typing import Dict

@dataclass
class OverrideMeta:
    score_path: str
    word_path: str
    delimiter: str = ","

    def extract(self) -> Dict[str, int]:
        tag_scores = {}
        with open(self.score_path, "r") as f:
            for line in f:
                tag, score, *rest = line.strip().split(self.delimiter)
                value = int(score)
                tag_scores[tag] = value

        result = {}
        with open(self.word_path, "r") as f:
            for line in f:
                word, *tags = line.strip().split(self.delimiter)
                key = word.upper().replace(" ", "")
                value = min(map(lambda t: tag_scores[t], tags))
                result[key] = value
        return result
