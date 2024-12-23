def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list) - 1

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2    # floor division operator (//): rounded-down integer value as the pivot index.
        pivot_value = the_list[pivot]

        if pivot_value == target:           # search is over, return the pivot(index)
            return pivot
        if pivot_value > target:            # higher than target, discard upper half of list  by setting upper bound to index just below pivot.
            upper_bound = pivot - 1
        else:                               # lower than target,  discard lower half of list  by setting lower bound to index just above pivot.
            lower_bound = pivot + 1

    return -1

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(test_list, 10))
print(binary_search(test_list, 4))
print(binary_search(test_list, 33))