import json
from typing import List, Dict

from overrides import OverrideMeta
from wordlists import WordlistEntry, WordlistMeta

CONFIG_PATH = "config.json"

def main(config_path: str):

    with open(config_path, "r") as f:
        config = json.loads(f.read())

    wordlists: List[List[WordlistEntry]] = []
    for wordlist_data in config["wordlists"]:
        wordlist_meta = WordlistMeta(**wordlist_data)
        wordlist = wordlist_meta.extract()
        wordlists.append(wordlist)

    combined = {}
    for wordlist in wordlists:
        for entry in wordlist:
            word = entry.word
            score = entry.score

            if word in combined:
                combined[word] = max(combined[word], score)
            else:
                combined[word] = score

    # Apply overrides
    overrides: List[List[WordlistEntry]] = []
    default_override_data = {
        "score_path": config["overrides"]["default_score_path"],
    }
    for override_data in config["overrides"]["data"]:
        override_meta = OverrideMeta(**default_override_data, **override_data)
        overrides.append(override_meta.extract())

    ocombined = {}
    for override in overrides:
        for entry in override:
            word = entry.word
            score = entry.score

            ocombined[word] = score

            # if word in combined:
            #     ocombined[word] = score
            # else:
            #     print(f"Warning: Cannot override unknown word: {word}")

    # Apply additions
    additions: List[List[WordlistEntry]] = []
    default_addition_data = {
        "score_path": config["additions"]["default_score_path"],
    }
    for addition_data in config["additions"]["data"]:
        addition_meta = OverrideMeta(**default_addition_data, **addition_data)
        additions.append(addition_meta.extract())

    acombined = {}
    for addition in additions:
        for entry in addition:
            word = entry.word
            score = entry.score

            acombined[word] = score

    # Write results to target files
    with open(config["out"]["base"], "w") as f:
        for word, score in sorted(combined.items()):
            f.write(f"{word};{score}\n")

    with open(config["out"]["overrides"], "w") as f:
        for word, score in sorted({**ocombined, **acombined}.items()):
            f.write(f"{word};{score}\n")

    with open(config["out"]["combined"], "w") as f:
        for word, score in sorted({**combined, **ocombined, **acombined}.items()):
            f.write(f"{word};{score}\n")

if __name__ == "__main__":
    main(CONFIG_PATH)
