# Implementing adding functionality.

def Addition(num1, num2):
    result = num1 + num2
    return result

def test_Add():
    assert Addition(20,30) == 50
    assert Addition(-20, 20) == 0