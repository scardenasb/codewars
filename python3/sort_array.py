# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while
# leaving the even numbers at their original positions.
#
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(arr):
    narr = []
    c = 0
    for i in arr:
        if i % 2 == 0:
            narr.append(i)
        else:
            narr.append(sorted(filter(lambda x: x % 2 != 0, arr))[c])
            c += 1
    return narr
