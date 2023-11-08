from kata_1 import kata_1
import pytest

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
    
def test_min():
    result = kata_1("20 6 627 1 min")
    assert result == 1

def test_max():
    result = kata_1("20 6 627 1 max")
    assert result == 627

def test_0_division():
    with pytest.raises(Exception, match="Erreur: division par 0 temptée!"):
        kata_1("1 0 /")
        
def test_small_stack():
    with pytest.raises(Exception, match="Erreur: vous avez besoin de plus d'un chiffre pour cette opération!"):
        kata_1("2 +")
        
def test_unknown_op():
    with pytest.raises(Exception, match="Erreur: cet opérande est inconnu!"):
        kata_1("2 5 + m")