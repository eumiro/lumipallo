from pathlib import Path

import pytest

from lumipallo import lumipallo as lp

TESTDATA = Path(__file__).with_name('testdata')


@pytest.fixture
def snow_01_loaded():
    snow = lp.Snow('deu')
    snow.load(*list(TESTDATA.glob('01_*.txt')))
    return snow


def test_frequency(snow_01_loaded):
    assert snow_01_loaded.most_common_words(3) == [('tom', 10), ('bruder', 8), ('heisst', 6)]


def test_wordindex(snow_01_loaded):
    assert len(snow_01_loaded.words) == 15
    assert snow_01_loaded.words['wie'] == {4, 16}
