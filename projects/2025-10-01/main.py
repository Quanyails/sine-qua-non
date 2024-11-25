import json
from typing import List, Dict

from overrides import OverrideMeta
from wordlists import WordlistMeta

CONFIG = "config.json"
DEST = "quanbined.dict"
SCORE_RANGE = (20, 50)

def main(config: str, dest: str):
    combined = {}

    with open(config, "r") as f:
        parsed = json.loads(f.read())

    # Take the highest score for each word
    wordlists: List[Dict[str, int]] = []
    for wordlist_data in parsed["wordlists"]:
        wordlist_meta = WordlistMeta(**wordlist_data)
        wordlist = wordlist_meta.extract()
        wordlists.append(wordlist)

    for wordlist in wordlists:
        for word, score in wordlist.items():
            if word in combined:
                combined[word] = max(combined[word], score)
            else:
                combined[word] = score

    # Apply overrides
    overrides: List[Dict[str, int]] = []
    for override_data in parsed["overrides"]:
        override_meta = OverrideMeta(**override_data)
        overrides.append(override_meta.extract())

    for override in overrides:
        for word, score in override.items():
            combined[word] = score

    # Trim low-scoring words
    scoremin, scoremax = SCORE_RANGE
    for word, score in list(combined.items()):
        if score < scoremin or score > scoremax:
            del combined[word]

    # Write results to target file
    with open(dest, "w") as f:
        for word, score in sorted(combined.items()):
            f.write(f"{word};{score}\n")

if __name__ == "__main__":
    main(CONFIG, DEST)
