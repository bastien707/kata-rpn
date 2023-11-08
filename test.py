from kata_1 import kata_1

def test_plus():
    result = kata_1("20 20 20 +")
    assert result == 60
    
def test_minus():
    result = kata_1("20 20 20 -")
    assert result == -20
    
def test_multi():
    result = kata_1("2 2 2 *")
    assert result == 8

def test_division():
    result = kata_1("6 3 2 /")
    assert result == 1

def test_all_op():
    result = kata_1("4 2 + 3 - 2 * 6 /")
    assert result == 1