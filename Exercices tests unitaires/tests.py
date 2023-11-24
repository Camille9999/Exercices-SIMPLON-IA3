from exercice import maxmin

def test_maxmin():
    assert maxmin('0') == '0 0'
    assert maxmin('-10') == '-10 -10'
    assert maxmin('1 1 1') == '1 1'
    assert maxmin('-1 -1 -1') == '-1 -1'
    assert maxmin('8 25 10 2') == '25 2'
    assert maxmin('-8 -25 -10 -2') == '-2 -25'
    assert maxmin('12 -4 8 55 0 -16 54 -15') == '55 -16'
