import pytest
from bank import value

def test_value():
    assert value("hello") =='$0'
    assert value("Hi") == '$20'
    assert value("What's up?") == "$100"
    assert value("hi") == '$20'

def test_upercase():
    assert value("HELLO") == '$0'
    assert value("WHAT'S UPP") =="$100"
    assert value("HI") == "$20"

#def test_whitespace():

def test_inteeger():
    with pytest.raises(AttributeError):
          value(125)

          
