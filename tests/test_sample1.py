import pytest

def test_file1_method1():
    x=5
    y=6
    assert x+1 == y,"test failed"
    assert x == y,"test failed"


def test_file1_method2():
    x=5
    y=6
    assert x+1 == y,"test failed without any reason! :)) "


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5