import copy
import json
from typing import Tuple, List, Dict

import postprocessors.nlp as nlppps
import postprocessors.postprocessors as pps

CONFIG_PATH = "config.json"
GAP = 2

type Entry = Tuple[str, int]

def insert_anywhere(s: str, insertion: str) -> List[str]:
    results = []
    # for i in range(0, len(s) + 1):
    for i in range(1, len(s)):
        inserted = s[:i] + insertion + s[i:]
        results.append(inserted)

    return results


def is_punny(word: str, allwordlist: set, anywordlist: set) -> bool:
    tokens = word.split(" ")

    if not all(len(token) >= 2 for token in tokens):
        return False

    # # Make sure tokens represent words we know
    if not all(word in allwordlist for word in tokens):
        return False

    if not any(word in anywordlist for word in tokens):
        return False
    #
    if len(tokens) > 2 or len(tokens[0]) < 4:
        return False

    return True


def main(config_path: str):
    with open(config_path, "r") as f:
        config = json.loads(f.read())

    entries: List[Entry] = []
    with open(config["out"]["combined"], "r") as f:
        for line in f:
            word, score, *_ = line.strip().split(";")
            key = word
            value = int(score)
            entries.append((key, value))

    # pun_postprocessor = nlppps.PunPostprocessor(max_similarity=0.1)
    good_words = set(word for word, score in entries if score >= 48)
    # punny_words = set(word for word, score in entries if pun_postprocessor.apply(word, score))
    non_stop_words = [word for word, score in entries if len(word) >= 3 and score >= 40]

    blank_space_postprocessors = [
        # remove all words that contain non-alphabetic characters (mainly, numbers)
        pps.LimitedAlphabetPostprocessor("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        pps.BlankSpacePostprocessor([
            # DRAW A (at index 2)
            pps.BlankSpaceMapping(blankable="D", index=GAP, replacewith="𝒹{0}"),
            pps.BlankSpaceMapping(blankable="R", index=GAP, replacewith="𝓇{0}"),
            pps.BlankSpaceMapping(blankable="A", index=GAP, replacewith="𝒶{0}"),
            pps.BlankSpaceMapping(blankable="W", index=GAP, replacewith="𝓌{0}"),
            # skip duplicate A

            # VERSE (at index 2)

            pps.BlankSpaceMapping(blankable="V", index=GAP, replacewith="𝓋{0}"),
            pps.BlankSpaceMapping(blankable="E", index=GAP, replacewith="𝑒{0}"),
            # skip duplicate R
            pps.BlankSpaceMapping(blankable="S", index=GAP, replacewith="𝓈{0}"),
            # skip duplicate E

            # POINT (at index -3)

            pps.BlankSpaceMapping(blankable="P", index=-GAP - 1, replacewith="{0}𝓅"),
            pps.BlankSpaceMapping(blankable="O", index=-GAP - 1, replacewith="{0}𝑜"),
            pps.BlankSpaceMapping(blankable="I", index=-GAP - 1, replacewith="{0}𝒾"),
            pps.BlankSpaceMapping(blankable="N", index=-GAP - 1, replacewith="{0}𝓃"),
            pps.BlankSpaceMapping(blankable="T", index=-GAP - 1, replacewith="{0}𝓉"),

            # SPACE (at index -3)

            pps.BlankSpaceMapping(blankable="S", index=-GAP - 1, replacewith="{0}𝓈"),
            pps.BlankSpaceMapping(blankable="P", index=-GAP - 1, replacewith="{0}𝓅"),
            pps.BlankSpaceMapping(blankable="A", index=-GAP - 1, replacewith="{0}𝒶"),
            pps.BlankSpaceMapping(blankable="C", index=-GAP - 1, replacewith="{0}𝒸"),
            pps.BlankSpaceMapping(blankable="E", index=-GAP - 1, replacewith="{0}𝑒"),
        ])
    ]
    carry_the_one_postprocessors = [
        pps.SplitDelimiterPostprocessor("ONE", good_words),
        nlppps.SegmentationPostprocessor(),
        nlppps.SegmentedWordFilterPostprocessor(["ANYONE", "EVERYONE", "ONE", "ONESELF", "SOMEONE"]),
    ]
    four_of_a_mind_postprocessors = [
        pps.RegexMatchPostprocessor(r"^[A-Z]{8,}$"),
        pps.UniqueLetterPostprocessor(max_required=4, min_required=4),
    ]
    its_all_wrong_singular_postprocessors = [
        # <noun>s <verb>
        pps.SplitDelimiterPostprocessor(
            wordlist=non_stop_words,
            delimiter="S",
        ),
        nlppps.SegmentationPostprocessor(),
        pps.RegexMatchPostprocessor(r"^.*S .*$"),
        nlppps.SegmentedWordFilterPostprocessor([ "DOWN", "OUT"]),
        nlppps.SegmentedSentencePostprocessor(),
    ]
    its_all_wrong_plural_postprocessors = [
        # <noun> <verb>s
        pps.RegexMatchPostprocessor(r"^.*S$"),
        nlppps.SegmentationPostprocessor(),
        pps.RegexMatchPostprocessor(r"^.\w* .\w*S$"),
        pps.FlatMapPostprocessor(lambda ts: [ts] if all(len(t) >= 3 for t in ts.split(" ")) else []),
        # We actually want all words where the singular == plural, so the logic sohuld be reversed.
        pps.FlatMapPostprocessor(lambda ts: [ts] if any(
            nlppps.PluralizablePostprocessor(reverse=True).apply(s, -1) for s in ts.split(" ")) else []),
        nlppps.SegmentedSentencePostprocessor(),
    ]
    no_cap_postprocessors = [
        pps.RegexMatchPostprocessor(r"^NO.*$"),
        pps.FlatMapPostprocessor(lambda s: ["NO" + s]),
        nlppps.SegmentationPostprocessor(),
        nlppps.SegmentedWordFilterPostprocessor(["NOBODY", "NOPE", "NOWHERE", "NODE", "NOUN", "NONE", "NOTHING"]),
        # nlppps.SegmentedFilterPostprocessor(lambda s: is_punny(s, good_words, punny_words)),
    ]
    seeing_stars_postprocessors = [
        pps.SubstringPostprocessor([
            result
            for star in ["ALTAIR", "ANTARES", "ARCTURUS", "CASTOR", "DENEB", "ORION", "POLLUX", "RIGEL", "SIRIUS", "SPICA", "VEGA"]
            for result in insert_anywhere(star, "C")
        ])
    ]
    postprocessors = [
        pps.LowScorePostprocessor(48),
        pps.MaxLengthPostprocessor(config["filters"]["max_length"]),
        *its_all_wrong_plural_postprocessors,
    ]

    postprocesseds: List[List[Entry]] = [copy.deepcopy(entries)]
    for postprocessor in postprocessors:
        wcurrent = postprocesseds[-1]
        wnext: List[Entry] = []
        for word, score in wcurrent:
            result = postprocessor.apply(word, score)
            wnext.extend(result)
        # Remove duplicates
        deduped: Dict[str, int] = {}
        for word, score in wnext:
            deduped[word] = score
        postprocesseds.append(list(deduped.items()))

    with open(config["out"]["postprocessed"], "w", encoding="utf8") as f:
        for word, score in sorted(postprocesseds[-1]):
            f.write(f"{word};{score}\n")


if __name__ == "__main__":
    main(CONFIG_PATH)
