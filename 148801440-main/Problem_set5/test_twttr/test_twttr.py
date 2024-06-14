import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Twitter") =='Twttr'
    assert shorten("Hello World") == 'Hll Wrld'
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == 'CS50'
    assert shorten("YOUR NAME?") == 'YR NM?'


def test_inteeger():
    with pytest.raises(TypeError):
          shorten(125)
