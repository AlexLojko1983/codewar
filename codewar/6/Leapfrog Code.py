# Implement a function `change_list(arr)` that takes a list as an argument and mutates its elements in such way:
# • If the element is an integer, square it
# • If the element is a string, append its reversed copy to its end like that "string" becomes "stringgnirts"
# • If the element is a bool, simply reverse it. True becomes False and False becomes True
# • Reverse the list
def change_list(*args):
    if not args:
        arr = list(input())[::2]
        return ''.join(arr)
    else:
        arr = args[0]
        for i in range(len(arr)):
            if type(arr[i]) is int: arr[i] = arr[i] ** 2
            elif type(arr[i]) is bool: arr[i] = not arr[i]
            elif type(arr[i]) is str: arr[i] = arr[i] + ''.join(arr[i][::-1])
            i = i+1
        arr = arr[::-1]
        return arr


print(change_list([3, 5, "hello", False, True, 9, "codewars", True]))
# print(change_list())
