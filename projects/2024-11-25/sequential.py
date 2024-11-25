import datetime
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Literal

import requests

from download import Download
from downloads import download


class SequentialSource(ABC):
    @abstractmethod
    def get_download(self) -> Download:
        pass

    @abstractmethod
    def increment(self, type: Literal["chapter", "page"]) -> None:
        pass


class Manga4Life(SequentialSource):
    # https://pyformat.info/
    BASE_PATH = r"D:/data/{title}/{chapter:04d}/{page:03d}.png"
    BASE_URL = "https://{host}/manga/{title}/{chapter:04d}-{page:03d}.png"

    def __init__(self, host: str, title: str, chapter: int = 1, page: int = 1):
        self.host = host
        self.title = title
        self.chapter = chapter
        self.page = page

        self.done = False

    def get_download(self) -> Download:
        filename = self.BASE_PATH.format(
            chapter=self.chapter, page=self.page, title=self.title
        )
        url = self.BASE_URL.format(
            chapter=self.chapter,
            host=self.host,
            page=self.page,
            title=self.title.title(),
        )
        return Download(
            path=Path(filename),
            url=url,
        )

    def increment(self, type: Literal["chapter", "page"]):
        # Don't try to increment a chapter if we just incremented a chapter.
        if type == "chapter" and self.page == 1:
            raise StopIteration
        elif type == "chapter" and self.page >= 1:
            self.chapter += 1
            self.page = 1
        elif type == "page":
            self.page += 1


def sequential_download(
        host: str,
        title: str,
        throttle: datetime.timedelta = datetime.timedelta(milliseconds=500),
):
    source = Manga4Life(host=host, title=title)

    while True:
        d = source.get_download()
        filename = str(d.path)
        url = d.url
        try:
            print(f"Downloading {url}...")
            download(d)
            print(f"Downloaded to {filename}")
            source.increment("page")

            # Add a small buffer to deter rate-limiting
            time.sleep(throttle.total_seconds())
        except requests.exceptions.HTTPError as e:
            print(f"Received HTTP {e.response.status_code}, continuing...")
            try:
                source.increment("chapter")
            except StopIteration:
                print(f"Cannot continue more.")
                break
        except IOError as e:
            print(f"Could not open file at {filename}.")
            raise e
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise e
    print("Done!")
