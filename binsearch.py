def binary_search(da_array: list, needle, left:int=0, right:int=-1):
    if left == 0:
        rangemin = 0
    else:
        rangemin = left
    if right == -1:
        rangemax=len(da_array) - 1
    else:
        rangemax=right
    while True:
        if rangemin > rangemax:
            index = -1
            return index
        #If rangemin and rangemax are both very high we do not want overflow,
        #so get the midpoint like this:
        midpoint = rangemin + (rangemax - rangemin)//2
        if da_array[midpoint] > needle:#lower part
            rangemax = midpoint - 1
            print("1!")
        elif da_array[midpoint] < needle:
            rangemin = midpoint + 1
            print("2!")
        else:
            index = midpoint
            return index

# binary_search([1,2,5,7,8,9], 7)
# ordered = [1,2,5,7,8,9]
# multiple = [1,1,1,1,2,2,2,3]
# unordered = [2,5,3,5,3,4,8]
# nothing = []
# one = [1]
# two = [2,3]
# nonNumeric = ['a','b']
# nan = [float('nan')]
# inf = [float("inf")]
# negative = [-6,-4,-2,-1,0,1,2,4]

# def test_left():
#     binary_search(ordered, 5,left=-1, right=-2)

#     binary_search(ordered, 5) == 2
#     # non numeric - TypeError
#     binary_search(nonNumeric, 5) == 2
#     # Empty array - -1
#     binary_search(nothing, 4)
#     # nan - -1
#     binary_search(nan, 1)
#     # boundaries
#     binary_search(ordered, 1)
#     binary_search(ordered, 9)
#     # Out of range needle
#     binary_search(ordered, 10)
#     binary_search(ordered, 0)
#     # multiple needles found
#     binary_search(multiple, 1)
#     # rangemax overflow
#     binary_search(ordered, 1, left=0, right=float("inf")+1)


# test_left()