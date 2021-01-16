"""Test corpus.py"""
import datetime as dt

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


def test_download_tatoeba_sentences_fresh_ok(requests_mock, tmp_path):
    """Test corpus downloads sentences from tatoeba"""
    now = dt.datetime.now(dt.timezone.utc)
    url = (
        "https://downloads.tatoeba.org"
        "/exports/per_language/deu/deu_sentences.tsv.bz2"
    )
    headers = {"Last-Modified": (now - dt.timedelta(days=1)).isoformat()}
    content = b"hello world"
    requests_mock.head(url, headers=headers)
    requests_mock.get(url, content=content)

    corpus = Corpus(data_dir=tmp_path)
    local_path = corpus.path / "deu_sentences.tsv.bz2"
    res = corpus._sync_tatoeba(local_path, url)
    assert requests_mock.call_count == 2
    assert res
    assert local_path.is_file()
    assert local_path.read_bytes() == content


def test_download_tatoeba_sentences_not_needed(requests_mock, tmp_path):
    """Test corpus does not download sentences from tatoeba if local"""
    now = dt.datetime.now(dt.timezone.utc)
    url = (
        "https://downloads.tatoeba.org"
        "/exports/per_language/deu/deu_sentences.tsv.bz2"
    )
    headers = {"Last-Modified": (now - dt.timedelta(days=1)).isoformat()}
    content = b"hello world"
    requests_mock.head(url, headers=headers)
    requests_mock.get(url, content=content)

    corpus = Corpus(data_dir=tmp_path)
    local_path = corpus.path / "deu_sentences.tsv.bz2"
    local_path.write_bytes(content)
    res = corpus._sync_tatoeba(local_path, url)
    assert requests_mock.call_count == 0
    assert not res
    assert local_path.is_file()
    assert local_path.read_bytes() == content


def test_download_tatoeba_sentences_tooold(requests_mock, tmp_path):
    """Test corpus does not downloads old sentences from tatoeba"""
    now = dt.datetime.now(dt.timezone.utc)
    url = (
        "https://downloads.tatoeba.org"
        "/exports/per_language/deu/deu_sentences.tsv.bz2"
    )
    headers = {"Last-Modified": (now - dt.timedelta(days=10)).isoformat()}
    content = b"hello world"
    requests_mock.head(url, headers=headers)
    requests_mock.get(url, content=content)

    corpus = Corpus(data_dir=tmp_path)
    local_path = corpus.path / "deu_sentences.tsv.bz2"
    res = corpus._sync_tatoeba(local_path, url)
    assert requests_mock.call_count == 1
    assert not res
    assert not local_path.is_file()
