from dataclasses import dataclass
from typing import List

from wordlist import WordlistEntry


@dataclass(frozen=True, slots=True)
class OverrideMeta:
    score_path: str
    word_path: str
    delimiter: str = ","
    sort: str = ""

    def extract(self) -> List[WordlistEntry]:
        tag_scores = {}
        with open(self.score_path, "r") as f:
            for line in f:
                tag, score, *rest = line.strip().split(self.delimiter)
                value = int(score)
                tag_scores[tag] = value

        seen = set()
        results = []
        with open(self.word_path, "r") as f:
            for line in f:
                word, *tags = line.strip().split(self.delimiter)

                if tags == [""]:
                    print(f"Missing tags for word: {word}")
                else:
                    token = word.upper().replace(" ", "")
                    value = max(map(lambda t: tag_scores[t], tags))

                if token in seen:
                    print(f"Duplicate entry for word: {word}")
                else:
                    seen.add(token)
                    entry = WordlistEntry(word=token, score=value)
                    results.append(entry)
        return results
