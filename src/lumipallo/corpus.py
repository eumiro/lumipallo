"""Corpus containing all sentences and links to translations."""

import datetime as dt
import typing
from pathlib import Path

import requests
import xdg
from dateutil import parser


class Corpus:
    """Corpus"""

    def __init__(self, data_dir: typing.Union[Path, None] = None):
        if data_dir is None:
            data_dir = xdg.xdg_data_home()
        self.path = data_dir / "lumipallo"
        self.path.mkdir(parents=True, exist_ok=True)

    def _sync_tatoeba(self, local_path: Path, url: str) -> bool:
        print(f"Checking {local_path} ")
        now = dt.datetime.now(dt.timezone.utc)
        too_old = now - dt.timedelta(days=7)
        if local_path.exists():
            mtime = dt.datetime.fromtimestamp(
                local_path.stat().st_mtime, dt.timezone.utc
            )
            if too_old < mtime:
                return False
        res = requests.head(url)
        res.raise_for_status()
        if parser.parse(res.headers["Last-Modified"]) < too_old:
            return False
        print(f"Downloading {url} ...", end="")
        res = requests.get(url)
        res.raise_for_status()
        local_path.write_bytes(res.content)
        print("OK")
        return True

    def update_tatoeba(
        self,
        src_langs: typing.List[str],
        target_langs: typing.List[str],
        local_root: Path,
    ) -> None:  # pragma: no cover
        url_root = "https://downloads.tatoeba.org/exports/per_language/"

        for lang in src_langs + target_langs:
            url_sentences = f"{url_root}/{lang}/{lang}_sentences.tsv.bz2"
            local_path = local_root / f"{lang}_sentences.tsv.bz2"
            self._sync_tatoeba(local_path, url_sentences)

        for src in src_langs:
            for target in target_langs:
                url_links = f"{url_root}/{target}/{target}-{src}_links.tsv.bz2"
                local_path = local_root / f"{target}-{src}_links.tsv.bz2"
                self._sync_tatoeba(local_path, url_links)
