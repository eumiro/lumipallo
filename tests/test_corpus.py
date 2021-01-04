"""Test corpus.py"""
from lumipallo.corpus import Corpus


def test_corpus_uses_xdg():
    """This should be the only test that uses the real XDG_DATA_DIR"""
    corpus = Corpus()
    assert corpus.path.is_dir()
    assert corpus.path.name == "lumipallo"


def test_corpus_empty(tmp_path):
    """Test corpus creates a new empty directory"""
    corpus = Corpus(data_dir=tmp_path)
    assert corpus.path.is_dir()
    assert not list(corpus.path.iterdir())
