# You are going to be given an array of integers.
# Your job is to take that array and find an index N where the sum of the integers
# to the left of N is equal to the sum of the integers to the right of N.
# If there is no index that would make this happen, return -1.

arr = [20, 10, 30, 10, 10, 15, 35]

#def find_even_index(arr):
    # for i in range(len(arr)):
    #     if sum(arr[:i]) == sum(arr[i+1:]):
    #         return i
    # return -1

def find_even_index(arr):
    arr_0 = []
    arr_1 = arr.copy()
    count = 0
    for i in arr:
        arr_1.remove(i)
        if sum(arr_0) == sum(arr_1):
            return count
        else:
            arr_0.append(i)
            count += 1
    return -1


print(find_even_index(arr))
