import pytest



def test_one_is_one():
    print('hello')
    assert 1 == 1


def test_two_is_two():
    assert 2 == 2

@pytest.mark.skip('Bug as')
def test_three_is_three():
    assert 3 == 3


test_one_is_one()
test_two_is_two()
test_three_is_three()
