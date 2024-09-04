# Implement a function `change_list(arr)` that takes a list as an argument and mutates its elements in such way:
# • If the element is an integer, square it
# • If the element is a string, append its reversed copy to its end like that "string" becomes "stringgnirts"
# • If the element is a bool, simply reverse it. True becomes False and False becomes True
# • Reverse the list
def change_list(arr):
    for i in arr:
        if type(i) is int: i = i ** 2
        if type(i) is bool: i = not i
        if type(i) is str: i = i + i[::-1]
        arr.reverse()
    return print(arr)
def some_func(arg1, arg2=None):
    change_list(arg1)
    arg2 = """
    def change_list(arr):
    for i in range(len(arr)):
        if type(arr[i]) is int: arr[i] = arr[i] ** 2
        elif type(arr[i]) is bool: arr[i] = not arr[i]
        elif type(arr[i]) is str: arr[i] = arr[i] + arr[i][::-1]
        i += 1
    arr = arr[::-1]
    return arr
        """
    return print(arg2[::2])

some_func([3, 5, "hello", False, True, 9, "codewars", True])