from upfpy import *

def test_factor():
    assert factor(3) == [0,1]
    assert factor(4) == [2]
    assert factor(5) == [0,0,1]
    assert factor(6) == [1,1]
    assert factor(7) == [0,0,0,1]
    assert factor(11) == [0,0,0,0,1]

