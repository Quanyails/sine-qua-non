from postprocessors import BlankSpaceMapping, LimitedAlphabetPostprocessor


def test_limited_alphabet():
    postprocessor = LimitedAlphabetPostprocessor("aeiou")

    result = postprocessor.apply("foobar", 1)
    assert result == []

    result = postprocessor.apply("iou", 1)
    assert result == [("iou", 1)]


def test_replacement_at_index():
    mapping = BlankSpaceMapping(blankable="b", index=-3, replacewith="1{0}")
    results = mapping.apply("foobarbaz")
    assert results == ["foobarbaz", "1foobaraz"]


if __name__ == "__main__":
    test_limited_alphabet()
    test_replacement_at_index()
