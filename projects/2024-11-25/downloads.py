import requests

from download import Download


def download(d: Download):
    r = requests.get(d.url, stream=True)
    r.raise_for_status()

    # If the download exists, make a file for it
    d.path.parent.mkdir(parents=True, exist_ok=True)
    d.path.touch()

    with open(d.path, mode="wb") as f:
        f.write(r.content)
