from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Downloadable:
    chapter: int
    page: int
    title: str


@dataclass(frozen=True)
class Download:
    path: Path
    url: str
