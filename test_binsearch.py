from pytest import raises
from binsearch import binary_search

ordered = [1,2,5,7,8,9]
multiple = [1,1,2,3]
unordered = [2,5,3,5,3,4,8]
nothing = []
one = [1]
two = [2,3]
nonNumeric = ['a', 'b']
nan = [float('nan')]
negative = [-6,-4,-2,-1,0,1,2,4]


def test_invalid_left_right():
    assert binary_search(ordered, 5,left=-1, right=-2) == -1

def test_regular():
    assert binary_search(ordered, 5) == 2

def test_nonnumeric():
    # non numeric - TypeError
    with raises(TypeError):
    	binary_search(nonNumeric, 5) == 2

def test_empty():
    assert binary_search(nothing, 4)==-1

def test_nan():
    assert binary_search(nan, 1) == 0

def test_negative():
	assert binary_search(negative, -4) == 1

def test_bound_left():
	assert binary_search(ordered, 1) == 0

def test_bound_right():
	assert binary_search(ordered, 9) == 5

def test_out_of_range():
	assert binary_search(ordered, 10) == -1

def test_out_of_range():
	assert binary_search(ordered, 0) == -1

# def test_multiple_found():
# 	assert binary_search(multiple, 1) == 5

#     # multiple needles found
#     binary_search(multiple, 1)
#     # rangemax overflow
#     binary_search(ordered, 1, left=0, right=float("inf")+1)


def test_char():
    with raises(TypeError):
        binary_search(nonNumeric, 3)
