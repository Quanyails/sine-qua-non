---
tags:
  - script
---

# Tumblr Tokenization Script

## Environment

- OS: Windows 11 21H2
- Python version: 3.10.6

## Code

```python
import re
import zipfile
from collections import Counter
from collections.abc import Generator
from html.parser import HTMLParser
from pathlib import Path
from typing import List

import click as click

POST_REGEX = re.compile(r"html/\d+\.html")
# Optional: replace this with a more robust tokenizer
TOKEN_REGEX = re.compile(r'[^\W\d]+')


class PostParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()

        self.posts: List[str] = []

    def handle_data(self, data: str) -> None:
        # replace this with a more robust HTML parser that ignores timestamps
        self.posts.append(data.strip())


def iterposts(path: Path) -> Generator[str, None, None]:
    with zipfile.ZipFile(path, "r") as archive:
        with archive.open("posts.zip") as posts_binary:
            with zipfile.ZipFile(posts_binary, "r") as posts_archive:
                posts = [
                    name for name in posts_archive.namelist()
                    if POST_REGEX.match(name)
                ]
                for name in posts:
                    with posts_archive.open(name) as post_binary:
                        bhtml = post_binary.read()
                        yield bhtml.decode()


@click.command()
@click.option("-i", "--in", "file_pathname",
              required=True,
              type=click.Path(
                  exists=True,
                  dir_okay=False,
              ))
def main(file_pathname: str):
    post_counter = PostParser()
    in_path = Path(file_pathname)

    for post in iterposts(in_path):
        post_counter.feed(post)

    # From here, you can extract and optionally save data from this data set.
    # Below are examples of data that can be extracted.

    words: Counter[str] = Counter()
    for post in post_counter.posts:
        words.update([t.lower() for t in TOKEN_REGEX.findall(post)])

    print("The total number of words on this Tumblr blog is:")
    print(words.total())

    print("The distribution of words on this Tumblr blog is:")
    for [word, count] in sorted(words.items(), key=lambda item: (-item[1], item[0])):
        print(word, count)


if __name__ == "__main__":
    main()
```

## How to use

1. [Export your Tumblr blog](https://help.tumblr.com/hc/en-us/articles/360005118894)
2. Run from the command line via `python tumblr_word_count.py -i path\to\file.zip`
3.
