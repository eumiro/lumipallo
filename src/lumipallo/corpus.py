"""Corpus containing all sentences and links to translations."""
import xdg


class Corpus:
    """Corpus"""

    def __init__(self, data_dir=None):
        if data_dir is None:
            data_dir = xdg.xdg_data_home()
        self.path = data_dir / "lumipallo"
        self.path.mkdir(parents=True, exist_ok=True)
