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

def test_one():
	assert binary_search(one, 1) == 0

def test_two():
	assert binary_search(two, 2) ==0 

def test_unordered():
	assert binary_search(unordered, 4) == 1

def test_invalid_left_right():
    assert binary_search(ordered, 5,left=-1, right=-2) == -1

def test_regular1():
    assert binary_search(ordered, 5) == 2

def test_regular2():
    assert binary_search(ordered, 7) == 3

def test_regular3():
    assert binary_search(ordered, 8) == 4

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

def test_not_array_set():
	with raises(TypeError):
		assert binary_search(set([1,3,5,6]), 3) == 1

def test_not_array_matrix():
	with raises(TypeError):
		assert binary_search([[1,2],[3,4]], 2) == 1

def test_not_array_dict():
	a = {1:2, 2:3}
	with raises(KeyError):
		assert binary_search(a, 1) == 0

# def test_multiple_found():
# 	assert binary_search(multiple, 1) == 5

#     # multiple needles found
#     binary_search(multiple, 1)
#     # rangemax overflow
def test_overflow():
    with raises(OverflowError):
    	binary_search(ordered, 1, left=0, right=int(float("inf")+1))


def test_char():
    with raises(TypeError):
        binary_search(nonNumeric, 3)
